import requests
import logging
from config.settings import OLLAMA_API_URL

logger = logging.getLogger(__name__)

class SummarizationAgent:
    def __init__(self):
        self.api_url = OLLAMA_API_URL
        self.model = "llama3.2:latest"

    def summarize(self, chunk):
        try:
            logger.info("Sending request to the Ollama API for summarization.")
            response = requests.post(
                f"{self.api_url}/generate",
                json={"model": self.model, "prompt": f"Summarize this legal text:\n{chunk}"}
            )
            response.raise_for_status()

            logger.info("Processing API response.")
            data = response.json()
            return data.get("response", "No summary generated.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error connecting to Ollama API: {e}")
            return "Error: Unable to generate summary."