import logging
from vector_store.chroma_store import ChromaStore
from utils.embedding_utils import EmbeddingUtils

logger = logging.getLogger(__name__)

def get_precedent_workflow():
    def precedent_workflow(summary):
        try:
            logger.info("Generating embedding for summary.")
            vector_store = ChromaStore()
            embedding_utils = EmbeddingUtils()
            embedding = embedding_utils.generate_embedding(summary)

            logger.info("Searching for precedents in the vector store.")
            results = vector_store.search(embedding, top_k=5)

            if not results:
                logger.warning("No precedents found.")
                return []
            return results
        except Exception as e:
            logger.error(f"Error in precedent workflow: {e}")
            return {"error": str(e)}
    return precedent_workflow