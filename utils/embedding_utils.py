from sentence_transformers import SentenceTransformer

class EmbeddingUtils:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

    def generate_embedding(self, text):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Text must be a non-empty string")
        return self.model.encode(text)

    def __repr__(self):
        return f"EmbeddingUtils(model_name={self.model_name})"