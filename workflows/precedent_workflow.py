from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableLambda
from vector_store.chroma_store import ChromaStore
from utils.embedding_utils import EmbeddingUtils

def get_precedent_workflow():
   
    chroma_store = ChromaStore()
    embedding_utils = EmbeddingUtils()

    
    prompt_preparation = RunnableLambda(
        lambda inputs: {
            "summary": inputs["summary"],
            "prompt": f"Find relevant legal precedents for the following summary:\n{inputs['summary']}"
        }
    )

    
    search_precedents = RunnableLambda(
        lambda inputs: chroma_store.search(
            embedding=embedding_utils.generate_embedding(inputs["summary"]),
            top_k=5
        )
    )

    
    workflow = RunnableSequence(prompt_preparation, search_precedents)

    return workflow