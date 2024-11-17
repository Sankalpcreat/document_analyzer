from chromadb import Client
from chromadb.config import Settings
import logging

logger = logging.getLogger(__name__)

class ChromaStore:
    def __init__(self, persist_dir="data/chroma"):
       
        try:
            logger.info("Initializing ChromaStore with persistence.")
            self.client = Client(Settings(persist_directory=persist_dir))
        except Exception as e:
            logger.error(f"Error initializing ChromaStore: {e}")
            raise

    def add_embedding(self, id, embedding, metadata=None):
        
        try:
            logger.info(f"Adding embedding to collection for ID: {id}")
            collection = self.client.get_or_create_collection(name="legal_vectors")
            collection.add(ids=[id], embeddings=[embedding], metadatas=[metadata])
            logger.info("Embedding added successfully.")
        except Exception as e:
            logger.error(f"Error adding embedding to ChromaStore: {e}")
            raise

    def search(self, embedding, top_k=5):
       
        try:
            logger.info("Searching for similar embeddings.")
            collection = self.client.get_collection(name="legal_vectors")
            results = collection.query(query_embeddings=[embedding], n_results=top_k)
            logger.info(f"Search completed. Found {len(results['ids'][0])} results.")
            return results
        except Exception as e:
            logger.error(f"Error during search in ChromaStore: {e}")
            return {"error": str(e)}

    def clear_collection(self):
        
        try:
            logger.info("Clearing the ChromaStore collection.")
            self.client.delete_collection(name="legal_vectors")
            logger.info("Collection cleared successfully.")
        except Exception as e:
            logger.error(f"Error clearing ChromaStore collection: {e}")
            raise