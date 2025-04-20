# MultiChat.ai

## 🌟 Our Mission

MultiChat.ai general-purpose AI assistant, using `LLMA_MODEL="llama-3.1-70b-versatile"`

## Prerequisites

- `> Python 3.8`
- Groq API key (required for `langchain-groq`)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/MultiChatNetwork/multichat-ai.git
cd multichat-ai
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the multichat-ai:

```bash
python3 src/run.py
```

## Flask API

```sh
curl -X POST http://127.0.0.1:5000/multichat-ai/input -H "Content-Type: application/json" -d '{"query": "Hi"}'
```

## Response

```json
{
  "response": "Hello! How can I assist you today?"
}
```

## Eroor

```json
{
  "error": "Query is required."
}
```

### 🤝 Contributing
We welcome contributions from everyone. If you're interested in contributing, please check out our [contribution guidelines](https://github.com/MultiChatNetwork/.github/blob/main/CONTRIBUTING.md).

### 🛡️ Security Issues

If you discover a security vulnerability within MultiChat, we would appreciate your help in disclosing it to us responsibly, please check out our [security issues guidelines](https://github.com/MultiChatNetwork/.github/blob/main/SECURITY.md).

### 🛡️ License
All our projects are released under the [MIT License](https://github.com/MultiChatNetwork/.github/blob/main/LICENSE).

### 🌐 Connect with Us
- **Website**: [www.multichat.network](https://www.multichat.network)
- **Email**: [multichat.network@gmail.com](mailto:multichat.network@gmail.com)
