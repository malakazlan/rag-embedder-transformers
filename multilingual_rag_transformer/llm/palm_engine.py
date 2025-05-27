import google.generativeai as genai

# You can set the API key globally or pass it per request

def get_genai_response(prompt: str, api_key: str, model: str = "gemini-2.0-flash-001") -> str:
    try:
        genai.configure(api_key=api_key)
        # Gemini models use the GenerativeModel class
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        # The response object has a 'text' attribute for the generated text
        return response.text.strip()
    except Exception as e:
        return f"[GenAI ERROR] {str(e)}" 