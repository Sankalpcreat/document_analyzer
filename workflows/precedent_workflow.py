from langchain.schema.runnable import RunnableSequence, RunnableLambda
from vector_store.chroma_store import ChromaStore
from utils.embedding_utils import EmbeddingUtils

def get_precedent_workflow():
    """
    Workflow to search for legal precedents using embeddings and a vector store.
    """
    # Initialize ChromaStore and EmbeddingUtils
    chroma_store = ChromaStore()
    embedding_utils = EmbeddingUtils()

    # Step 1: Prepare the prompt
    prompt_preparation = RunnableLambda(
        lambda inputs: {
            "summary": inputs["summary"],
            "prompt": f"Find relevant legal precedents for the following summary:\n{inputs['summary']}"
        }
    )

    # Step 2: Search for precedents
    search_precedents = RunnableLambda(
        lambda inputs: chroma_store.search(
            embedding_utils.generate_embedding(inputs["summary"]), top_k=5
        )
    )

    # Combine steps into a sequence
    workflow = RunnableSequence(
        prompt_preparation | search_precedents
    )

    return workflow