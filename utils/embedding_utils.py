from sentence_transformers import SentenceTransformer

class EmbeddingUtils:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_embedding(self, text):
        return self.model.encode(text)