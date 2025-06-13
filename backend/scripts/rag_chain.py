import os
from dotenv import load_dotenv
import google.generativeai as genai

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

# Load .env from the backend folder
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # goes to /backend
dotenv_path = os.path.join(project_root, ".env")
load_dotenv(dotenv_path)

# Configure Gemini LLM
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def load_documents():
    docs = []
    data_path = os.path.join(project_root, "data")

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"The data folder was not found: {data_path}")

    print("📁 Looking for files in:", data_path)

    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                docs.append(Document(page_content=f.read()))
    return docs

def build_vectorstore():
    texts = load_documents()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(texts)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb_path = os.path.join(project_root, "vectordb")
    db = FAISS.from_documents(split_docs, embeddings)
    db.save_local(vectordb_path)
    return db

def load_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb_path = os.path.join(project_root, "vectordb")
    return FAISS.load_local(vectordb_path, embeddings)

def query_rag(question):
    db = load_vectorstore()
    qa = RetrievalQA.from_chain_type(
        llm=genai.GenerativeModel("gemini-pro"),
        retriever=db.as_retriever(),
        return_source_documents=False
    )
    return qa.run(question)

if __name__ == "__main__":
    build_vectorstore()
