from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("C:\RAG_Chatbot\Dipro2.pdf")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = text_splitter.split_documents(docs)

embeddings= OllamaEmbeddings(model="gemma:2b")

verctor = FAISS.from_documents(split_docs, embeddings)

retriever = verctor.as_retriever()

prompt = ChatPromptTemplate([(
    """
You have to act like Shoaib. Your bio will be given in the context.People will ask question to you and 
answer the questions based on the provided context only. 
Please provide the most accurate response based on the question and answer in short.
<context>
{context}
<context>
Ouestion: {input}
Answer:
""")

])

llm= ChatGroq(model="llama-3.1-8b-instant")

