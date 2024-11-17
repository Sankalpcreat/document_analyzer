import requests

def call_ollama(prompt, model="llama-3.2"):
    try:
        response = requests.post(
            "http://localhost:11434/generate",
            json={"model": model, "prompt": prompt}
        )
        response.raise_for_status()
        return response.json().get("response", "No response")
    except requests.exceptions.RequestException as e:
        print(f"Error calling Ollama API: {e}")
        return "Error"