import requests

def get_llm_response(prompt: str, model="deepseek-r1"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        data = response.json()
        print("Ollama raw response:", data)  # Debug print for development
        return data.get("response", "").strip()
    except Exception as e:
        return f"[LLM ERROR] {str(e)}"