from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain #chain for documents
from langchain.chains import create_retrieval_chain #chain for retrieval
import streamlit as st

from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("C:\\RAG_Chatbot\\Dipro1.pdf")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
split_docs = text_splitter.split_documents(docs)

embeddings= OllamaEmbeddings(model="gemma:2b")

vector = FAISS.from_documents(split_docs, embeddings)

retriever = vector.as_retriever()

prompt = ChatPromptTemplate([(
    """
You have to act like Diprodip. Your bio will be given in the context.People will ask question to you and 
answer the questions based on the provided context only. 
Please provide the most accurate response based on the question and answer in short.
<context>
{context}
</context>
Question: {input}
Answer:
""")

])

llm= ChatGroq(model="llama-3.1-8b-instant")

question= "What is your name?"

document_chain= create_stuff_documents_chain(llm,prompt)
retrieval_chain= create_retrieval_chain(retriever, document_chain) 



st.header("Dipro Chatbot")
input=st.text_input("Ask a question to Dipro:")
if st.button("Get Answer"):
    response = retrieval_chain.invoke({'input': input})
    st.write(response["answer"])