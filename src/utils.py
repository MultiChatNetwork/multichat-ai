"""
(c) 2024 MultiChat. All rights reserved.
Unauthorized use prohibited.
Website: https://www.multichat.network
"""

import logging

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

# File handler
fileHandler = logging.FileHandler('multichat-ai.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


def logMessage(level: str, message: str):
    if level == 'info':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.debug(message)


def printMessage(message: str):
    print(message)
