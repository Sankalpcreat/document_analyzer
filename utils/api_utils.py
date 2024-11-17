import requests
from config.settings import OLLAMA_API_URL  

def call_ollama(prompt, model="llama-3.2"):
    try:
        response = requests.post(
            f"{OLLAMA_API_URL}/generate",
            json={"model": model, "prompt": prompt}
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response available")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling Ollama API: {e}")
        return "Error: Unable to fetch response"
    except ValueError:
        logging.error("Invalid JSON response from Ollama API")
        return "Error: Invalid API response"