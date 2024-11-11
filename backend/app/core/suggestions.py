import requests
from app.config import config

def get_improvement_suggestions(text):
    api_key = config.API_KEY
    if not api_key:
        raise ValueError("API key not found in config. Please set the API_KEY in the config file.")

    headers = {"Authorization": f"Bearer {api_key}"}
    prompt = (
        f"Please provide detailed suggestions to enhance the quality and readability of the following content. "
        f"Offer tips to improve user engagement, informativeness, and SEO. "
        f"Focus on clarity, relevant keywords, structure, and search engine optimization. "
        f"Here is the content:\n\n{text}\n\n"
        f"Provide specific actions to take for each suggestion."
    )

    payload = {
        "prompt": prompt,
        "max_tokens": 200,  # Increased max tokens for more detailed suggestions
        "temperature": 0.5,  # Lower temperature for more focused and coherent suggestions
    }

    try:
        response = requests.post("https://api.cohere.ai/v1/generate", headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        suggestions = response.json().get("generations", [{}])[0].get("text", "")
        return {"suggestions": suggestions}
    except requests.exceptions.RequestException as e:
        raise SystemError(f"An error occurred during the API request: {e}")
    except IndexError:
        raise SystemError("API response is missing required data.")
    except Exception as e:
        raise SystemError(f"An unexpected error occurred: {e}")
