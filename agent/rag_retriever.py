
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_DB_DIR = "vectorstore"

def retrieve_context(query: str, k: int = 3) -> str:
    """
    Retrieve relevant knowledge chunks for a given query
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embeddings
    )

    docs = vectordb.similarity_search(query, k=k)

    context = "\n\n".join([doc.page_content for doc in docs])
    return context
