import pinecone
from config.settings import PINECONE_API_KEY, PINECONE_INDEX

class PineconeStore:
    def __init__(self):
        pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")
        self.index = pinecone.Index(PINECONE_INDEX)

    def add_embedding(self, id, embedding, metadata=None):
        self.index.upsert([(id, embedding, metadata)])

    def search(self, embedding, top_k=5):
        return self.index.query(embedding, top_k=top_k)