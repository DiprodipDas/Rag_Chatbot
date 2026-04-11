
 # 🤖 RAG Chatbot - Q&A System using Retrieval-Augmented Generation(RAG)

A powerful Q&A chatbot that combines document retrieval with large language models to provide accurate, context-aware answers. The system uses RAG (Retrieval-Augmented Generation) to fetch relevant information from PDF documents and generates responses using Groq's Llama 3.1 model.

## 📌 Project Description

This is a sophisticated Q&A chatbot built using **Retrieval-Augmented Generation (RAG)** technology. The chatbot:
- 📄 Extracts information from PDF documents
- 🔍 Retrieves relevant content using semantic search
- 💡 Generates accurate answers using  llama-3.1-8b-instant via Groq API
- 🎯 Provides context-aware responses based on your documents

The project is implemented using the **LangChain** framework and features a user-friendly **Streamlit** interface.

## 🚀 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **LangChain** | RAG framework and orchestration |
| **Ollama** | Local embeddings generation (Gemma 2B) |
| **FAISS** | Vector database for similarity search |
| **Groq API** | LLM inference (Llama 3.1 8B Instant) |
| **Streamlit** | Web interface |
| **PyPDF** | PDF document processing |

## 📋 Prerequisites

- Python 3.8 or higher
- Ollama installed locally ([Download Ollama](https://ollama.ai/))
- Groq API key ([Get API key](https://console.groq.com/))
- Git (for cloning)

## 🛠 Installation & Setup

### 1. Fork the Repository
Click the **Fork** button at the top right of the GitHub repository page to create a copy in your account.

### 2. Clone the Repository
```bash
git clone https://github.com/DiprodipDas/Rag_Chatbot.git
```

### 3. Create a Virtual Environment
```bash
 python -m venv myenv  # For Windows/Linux/Mac
 source myenv/bin/activate  # Mac/Linux
 myenv\Scripts\activate  # Windows
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Install and Set Up Ollama
```bash
ollama pull gemma:2b
```

### 6. Set Up Environment Variables
```bash
GROQ_API_KEY=your_groq_api_key
```

### 7. Add Your PDF Document
```bash
loader = PyPDFLoader(r"C:\your_path\document.pdf")
```

### 8. Run the Chatbot
```bash
streamlit run chatbot.py
```

### WorkFlow
```bash
┌─────────────┐
│   PDF Input │
└──────┬──────┘
       ↓
┌─────────────┐
│ Text Split  │ → Chunking into smaller pieces
└──────┬──────┘
       ↓
┌─────────────┐
│  Embeddings │ → Ollama (gemma:2b)
└──────┬──────┘
       ↓
┌─────────────┐
│ FAISS Store │ → Vector database
└──────┬──────┘
       ↓
┌─────────────┐
│   Query     │ → User question
└──────┬──────┘
       ↓
┌─────────────┐
│  Retrieval  │ → Similarity search
└──────┬──────┘
       ↓
┌─────────────┐
│  Generation │ → Groq (Llama 3.1 8B Instant)
└──────┬──────┘
       ↓
┌─────────────┐
│   Answer    │ → Response to user
└─────────────┘
```


### 🤝 Contributors
```bash
Diprodip Das
```










