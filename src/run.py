"""
(c) 2024 MultiChat. All rights reserved.
Unauthorized use prohibited.
Website: https://www.multichat.network
"""

import os
import atexit
from typing import List

from flask import Flask, request, jsonify
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.runnables.history import (
    RunnableWithMessageHistory,
    BaseChatMessageHistory,
)
from langchain_core.messages import BaseMessage

from utils import logMessage, printMessage

load_dotenv()


app = Flask(__name__)


class InMemoryHistory(BaseChatMessageHistory):
    """
    In-memory implementation of chat message history.
    """

    def __init__(self):
        self.messages: List[BaseMessage] = []

    def addMessages(self, messages: List[BaseMessage]) -> None:
        self.messages.extend(messages)

    def addMessage(self, message: BaseMessage) -> None:
        self.messages.append(message)

    def clear(self) -> None:
        self.messages.clear()


class MultiChatAI:
    description = os.getenv("MULTICHAT_AI_DESC")

    def __init__(self, description: str = description):
        printMessage("Welcome to MultiChat.ai!")

        self.groqApiKey = os.getenv("GROQ_API_KEY")
        self.llmModel = os.getenv("LLMA_MODEL")

        if not self.groqApiKey:
            logMessage("error", "GROQ API key is not set.")
            raise ValueError("GROQ API key is not set.")

        self.llm = ChatGroq(
            model=self.llmModel, temperature=0.7, groq_api_key=self.groqApiKey
        )

        # Initialize the in-memory history
        self.sessionHistory = InMemoryHistory()

        def getSessionHistory() -> BaseChatMessageHistory:
            return self.sessionHistory

        self.conversation = RunnableWithMessageHistory(
            runnable=self.llm, get_session_history=getSessionHistory
        )

        self.description = description

    def greet(self):
        return "Hi, I'm MultiChat AI, how can i assist you !"

    def startConversation(self):
        greeting = self.greet()
        print(greeting)

    def getResponse(self, userInput: str) -> str:
        context = f"{self.description}\n\nUser question: {userInput}"
        responseContent = "Error generating response."

        try:
            response = self.conversation.invoke(input=context)
            responseContent = response.content
        except Exception as error:
            logMessage("error", f"Error in getResponse: {str(error)}")

        cleanup()

        return responseContent


@app.route('/multichat-ai/input', methods=['POST'])
def handleInput():
    data = request.json
    userInput = data.get("query")

    if not userInput:
        return jsonify({"error": "Query is required."}), 400

    try:
        response = multiChatAI.getResponse(userInput)
        return jsonify({"response": response})
    except Exception as e:
        logMessage("error", f"Exception in handleInput: {str(e)}")
        return jsonify({"error": "Internal server error."}), 500
    finally:
        cleanup()


def cleanup():
    # logMessage("info", "Application is shutting down.")
    multiChatAI.sessionHistory.clear()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)

    try:
        multiChatAI = MultiChatAI()
        multiChatAI.startConversation()
    except ValueError as error:
        logMessage("error", str(error))
        exit(1)

    atexit.register(cleanup)

    SERVER_PORT = os.getenv("SERVER_PORT", 3000)
    app.run(
        port=SERVER_PORT,
        debug=False,
    )
