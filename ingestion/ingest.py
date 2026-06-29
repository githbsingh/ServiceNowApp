from ingestion.document_loader import DocumentLoader
from ingestion.chunking import create_chunks
from vectorstore.chroma_manager import ChromaManager
from utils.logger import logger

def main():

    loader = DocumentLoader()

    full_text = loader.load_documents()



    #print(f"Loaded {len(documents)} pages")
    logger.info(f"Loaded {len(full_text)} pages")


    chunks = create_chunks(
        full_text
    )
    
    if len(chunks) == 0:
        logger.error("No chunks created. Check PDF loading.")
        return


    logger.info(f"Created {len(chunks)} chunks")
    logger.info(f"chunks: {chunks}")

    chroma = ChromaManager()

    chroma.create_vector_store(
        chunks
    )

    logger.info("Knowledge Base Created successfully")


if __name__ == "__main__":
    main()