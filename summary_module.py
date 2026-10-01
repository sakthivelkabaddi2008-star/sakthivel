from gemini_client import generate_text


def summarize_text(text: str) -> str:
    text = text.strip()
    if not text:
        return "Please enter text to summarize."

    prompt = f"""
Summarize the following educational text for quick revision.
Keep the main facts and important context.
Use simple language and bullet points where useful.
Do not invent information.

Text:
{text}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to summarize right now: {exc}"
