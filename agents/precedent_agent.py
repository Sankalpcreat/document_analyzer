from vector_store.chroma_store import ChromaStore
from utils.embedding_utils import EmbeddingUtils

class PrecedentAgent:
    def __init__(self):
        self.vector_store = ChromaStore()
        self.embedding_utils = EmbeddingUtils()

    def find_precedents(self, summary):
        embedding = self.embedding_utils.generate_embedding(summary)
        results = self.vector_store.search(embedding, top_k=5)
        return results