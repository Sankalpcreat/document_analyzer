import requests  
from config.settings import OLLAMA_API_URL

class SummarizationAgent:
    def __init__(self):
        self.api_url = OLLAMA_API_URL

    def summarize(self, chunk):
        try:
            response = requests.post(
                f"{self.api_url}/generate",
                json={"model": "llama-3.2", "prompt": f"Summarize this legal text:\n{chunk}"}
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "No summary generated.")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Ollama API: {e}")
            return "Error: Unable to generate summary."