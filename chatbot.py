from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:\RAG_Chatbot\Dipro2.pdf")
docs = loader.load()