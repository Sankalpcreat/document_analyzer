from vector_store.chroma_store import ChromaStore
from utils.embedding_utils import EmbeddingUtils
import logging

logger = logging.getLogger(__name__)

class PrecedentAgent:
    def __init__(self):
        self.vector_store = ChromaStore()
        self.embedding_utils = EmbeddingUtils()

    def find_precedents(self, summary):
        try:
            logger.info("Generating embedding for summary.")
            embedding = self.embedding_utils.generate_embedding(summary)

            logger.info("Searching for precedents in the vector store.")
            results = self.vector_store.search(embedding, top_k=5)

            if not results:
                logger.warning("No precedents found.")
                return []
            return results
        except Exception as e:
            logger.error(f"Error finding precedents: {e}")
            return {"error": str(e)}