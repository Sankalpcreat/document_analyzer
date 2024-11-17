from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

def get_summarization_workflow():
    prompt = PromptTemplate.from_template(
        "Summarize this legal document:\n{summary}"
    )
    llm = OllamaLLM(model="llama3.2:latest")

    # Use the pipe operator to chain prompt and llm
    workflow = prompt | llm

    return workflow