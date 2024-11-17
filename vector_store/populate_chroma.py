from vector_store.chroma_store import ChromaStore
from utils.embedding_utils import EmbeddingUtils
import logging

logger = logging.getLogger(__name__)

def populate_chroma_store(documents):
    """
    Populates the ChromaStore with embeddings for provided documents.

    Args:
        documents (list of dict): A list of dictionaries, each containing a document with keys 'id' and 'text'.
    """
    chroma_store = ChromaStore()
    embedding_utils = EmbeddingUtils()

    for idx, doc in enumerate(documents):
        try:
            logger.info(f"Processing document {idx + 1}/{len(documents)}: {doc['id']}")
            embedding = embedding_utils.generate_embedding(doc["text"])
            chroma_store.add_embedding(id=doc["id"], embedding=embedding, metadata=doc)
            logger.info(f"Document {doc['id']} added successfully.")
        except Exception as e:
            logger.error(f"Error adding document {doc['id']}: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example data to populate
    documents = [
        {"id": "doc_1", "text": "This is the first legal document about social control."},
        {"id": "doc_2", "text": "This document discusses primitive justice and legal frameworks."},
        {"id": "doc_3", "text": "An analysis of punitive measures in ancient societies."},
    ]

    logger.info("Starting population of ChromaStore.")
    populate_chroma_store(documents)
    logger.info("Population completed.")