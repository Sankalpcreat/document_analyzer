import requests
import logging

logger = logging.getLogger(__name__)

def call_ollama(prompt, model="llama3.2:latest"):
    try:
        logger.info("Calling Ollama API.")
        response = requests.post(
            "http://localhost:11434/generate",
            json={"model": model, "prompt": prompt}
        )
        response.raise_for_status()
        return response.json().get("response", "No response.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling Ollama API: {e}")
        return "Error"