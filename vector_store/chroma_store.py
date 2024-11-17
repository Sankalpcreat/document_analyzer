from chromadb import Client
from chromadb.config import Settings

class ChromaStore:
    def __init__(self, persist_dir="data/chroma"):
        # Initialize Chroma client with persistence
        self.client = Client(Settings(persist_directory=persist_dir))
        self.collection_name = "legal_vectors"

        # Ensure the collection exists during initialization
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def add_embedding(self, id, embedding, metadata=None):
        """
        Add a new embedding to the collection with metadata.
        """
        self.collection.add(
            ids=[id],
            embeddings=[embedding],
            metadatas=[metadata if metadata else {}]
        )

    def search(self, embedding, top_k=5):
        """
        Perform a similarity search on the collection using the given embedding.
        """
        try:
            # Ensure the collection exists
            collection = self.client.get_collection(name=self.collection_name)
            return collection.query(query_embeddings=[embedding], n_results=top_k)
        except Exception as e:
            # Handle errors gracefully
            raise ValueError(f"Error during search: {str(e)}. Ensure the collection is populated with embeddings.")