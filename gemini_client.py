import os
from functools import lru_cache

from google import genai
from google.genai import types


@lru_cache(maxsize=1)
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Create a .env file and add your Gemini API key."
        )
    return genai.Client(api_key=api_key)


def generate_text(prompt: str) -> str:
    model = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
    response = get_client().models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
        ),
    )
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
