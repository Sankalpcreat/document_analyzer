from vector_store.chroma_store import ChromaStore
from utils.embedding_utils import EmbeddingUtils

def populate_chroma_store(precedents):
    """
    Populate the ChromaStore with legal precedents.
    
    :param precedents: List of tuples (id, text, metadata)
    """
    chroma_store = ChromaStore()
    embedding_utils = EmbeddingUtils()

    for precedent_id, text, metadata in precedents:
        embedding = embedding_utils.generate_embedding(text)
        chroma_store.add_embedding(id=precedent_id, embedding=embedding, metadata=metadata)
        print(f"Added precedent {precedent_id} to ChromaStore")

if __name__ == "__main__":
    # Example precedents
    precedents = [
        ("precedent_1", "Legal precedent text 1", {"case": "Case 1", "year": 2000}),
        ("precedent_2", "Legal precedent text 2", {"case": "Case 2", "year": 2005}),
    ]
    populate_chroma_store(precedents)