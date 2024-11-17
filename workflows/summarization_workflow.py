from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain.schema.runnable import RunnableSequence

def get_summarization_workflow():
  
    prompt = PromptTemplate.from_template(
        "Summarize the following legal document:\n{summary}"
    )

    
    llm = Ollama(model="llama3.2:latest")

    
    workflow = RunnableSequence(prompt, llm)

    return workflow