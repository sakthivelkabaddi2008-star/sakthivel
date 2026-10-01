from gemini_client import generate_text


def answer_question(question: str) -> str:
    question = question.strip()
    if not question:
        return "Please enter a question."

    prompt = f"""
You are EduGenie, an educational assistant.
Answer the student's question accurately and concisely.
Use simple language and short paragraphs.
If the question is ambiguous, state the assumption you are making.

Student question:
{question}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to answer right now: {exc}"
