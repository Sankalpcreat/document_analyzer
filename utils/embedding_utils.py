from sentence_transformers import SentenceTransformer
import logging

logger = logging.getLogger(__name__)

class EmbeddingUtils:
    def __init__(self):
       
        try:
            logger.info("Loading SentenceTransformer model for embeddings.")
            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            logger.info("SentenceTransformer model loaded successfully.")
        except Exception as e:
            logger.error(f"Error initializing SentenceTransformer: {e}")
            raise

    def generate_embedding(self, text):
        
        try:
            logger.info("Generating embedding for the provided text.")
            return self.model.encode(text)
        except Exception as e:
            logger.error(f"Error generating embedding: {e}")
            raise