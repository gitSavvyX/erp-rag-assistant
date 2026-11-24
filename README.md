# ERP RAG Assistant | Intelligent Business Analytics

An AI-powered assistant that enables users to query complex ERP business data (Sales, Inventory, and Finance) using natural language. Built to transform static business databases into conversational insights using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

## 📖 Overview
Traditional ERP systems require users to know SQL or navigate complex dashboards to retrieve business insights. This project bridges that gap by allowing managers to ask plain English questions (e.g., *"What were the total sales in October?"* or *"Is our laptop inventory low?"*). The AI agent securely retrieves the relevant data, processes it, and generates an accurate, context-aware answer.

## 🚀 Core Features
• **Natural Language Querying:** Ask questions about sales and inventory without writing SQL.
• **Contextual Retrieval:** Uses RAG to fetch only the most relevant business data before sending it to the LLM.
• **Business Intelligence:** Instantly identifies low stock, high-performing products, and revenue trends.
• **Secure API Integration:** Designed to integrate with backend systems via REST APIs.

## 🛠️ Tech Stack
| Category | Technologies |
| :--- | :--- |
| Programming | Python |
| AI & LLMs | LangChain, OpenAI API, RAG, Prompt Engineering |
| Data Processing | Pandas, NumPy |
| Vector Database | FAISS (for semantic data retrieval) |

## ⚙️ How it Works
1. **Data Ingestion:** The system loads ERP data (mock CSV/SQL tables for Sales and Inventory).
2. **Embedding:** The data is converted into vector embeddings using an embedding model.
3. **Retrieval:** When a user asks a question, the system searches the vector database (FAISS) for the most relevant data chunks.
4. **Generation:** The retrieved business data and the user's question are sent to the LLM (OpenAI), which generates a precise, human-readable answer.

## 💻 Setup & Installation
To run this project locally, follow these steps:

1. Clone the repository:
   `git clone https://github.com/gitSavvyX/erp-rag-assistant.git`
2. Navigate to the project directory:
   `cd erp-rag-assistant`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Set your OpenAI API key:
   `export OPENAI_API_KEY="your_api_key_here"`
5. Run the assistant:
   `python main.py`

## 💡 Example Interaction
**User Question:** "What were the total sales in October and is our laptop inventory low?"

**AI Assistant Answer:** "In October, the total sales amounted to 66,500 PKR (Laptop: 50,000 | Monitor: 12,000 | Keyboard: 3,000 | Mouse: 1,500). Yes, the laptop inventory is currently low, with only 20 units remaining in stock."

## 🔒 Security & Privacy
• API keys are managed via environment variables.
• No sensitive client data is stored in the repository. Mock data is used for demonstration.
