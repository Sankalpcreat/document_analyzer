from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain.schema.runnable import RunnableSequence

def get_risk_workflow():
   
    prompt = PromptTemplate.from_template(
        "Analyze the following legal text for potential risks and assign a risk score:\n{summary}"
    )

    
    llm = Ollama(model="llama3.2:latest")

    
    workflow = RunnableSequence(prompt, llm)

    return workflow