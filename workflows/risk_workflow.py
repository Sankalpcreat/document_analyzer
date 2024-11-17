from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

def get_risk_workflow():
    prompt = PromptTemplate.from_template(
        "Analyze the following legal text for potential risks and assign a risk score:\n{summary}"
    )
    llm = OllamaLLM(model="llama3.2:latest")

    # Use the pipe operator to chain prompt and llm
    workflow = prompt | llm

    return workflow