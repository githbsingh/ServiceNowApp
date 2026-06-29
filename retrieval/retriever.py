from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from utils.logger import logger


def retrieve_context(query):

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    logger.info(f"Query: {query}")

    docs = db.similarity_search(
    "severity",
    k=1,
    filter={
        "section":
            "3. SEVERITY CLASSIFICATION"
    }
)

    logger.info(f"Retrieved {len(docs)} chunks")
    logger.info(f"Retrieved chunks: {docs}")

    # return "\n".join(
    #     [
    #         doc.page_content
    #         for doc in docs
    #     ]
    # )
    return docs