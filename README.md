# 🧠 AI Agent With Long-Term Memory

A modular AI Agent architecture that integrates **long-term memory**, **retrieval-augmented generation (RAG)**, and **Zep memory server**, enabling persistent and contextual conversation over extended sessions. Powered by OpenAI's `autogen` framework.

## 🚀 Features

- 🧠 **Long-Term Memory Integration** via [Zep](https://docs.getzep.com/)
- 💬 **Conversational Agents** built using [AutoGen](https://github.com/microsoft/autogen)
- 🔁 **Memory Retrieval & Fact Ingestion**
- 📁 **Local & Remote File Context** support
- 🧩 **Modular & Extensible Design**

## 🏗️ Architecture

User ↔ ConversableAgent ↔ AssistantAgent
↕ ↕
Memory Code Execution
(Zep) (Optional)


- Agents can query Zep to **recall facts**, and **store new knowledge**.
- Uses OpenAI's GPT models for reasoning and conversation.

## 📦 Installation

```bash
git clone https://github.com/jeevangowda1718/AI-Agent-With-Long-Term-Memory.git
cd AI-Agent-With-Long-Term-Memory
pip install -r requirements.txt

⚙️ Configuration

    Set up environment variables:

        OPENAI_API_KEY

        ZEP_API_KEY (if using hosted Zep)

        ZEP_URL (e.g., http://localhost:8000 if running locally)

You can store these in a .env file:

OPENAI_API_KEY=your-openai-api-key
ZEP_API_KEY=your-zep-api-key
ZEP_URL=http://localhost:8000

    Run Zep Server (if using locally):

docker run -p 8000:8000 ghcr.io/getzep/zep:latest

🧪 Usage
Conversable Agent with Zep Memory

python contrib/zep_conversable_agent.py

The agent will:

    Store memories from user interactions

    Recall relevant facts using vector search

    Provide contextual and long-term responses

📁 Directory Structure

AI-Agent-With-Long-Term-Memory/
├── contrib/
│   └── zep_conversable_agent.py  # Main agent entry point
├── utils/
│   └── memory.py                 # Zep memory wrapper
├── .env                          # API keys & config
├── requirements.txt
└── README.md

📚 References

    AutoGen by Microsoft

    Zep Memory Server

🤝 Contributing

Contributions, ideas, and issues are welcome! Feel free to open a pull request or issue.
📜 License


    Built with 💡 by Jeevan Gowda
