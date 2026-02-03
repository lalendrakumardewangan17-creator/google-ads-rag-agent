from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

VECTOR_DB_DIR = "vectorstore"

def ingest_knowledge():
    documents = []

    knowledge_path = "data/knowledge"
    for file in os.listdir(knowledge_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(knowledge_path, file))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )

    
    print("✅ Knowledge ingestion completed")
