import json
import re

from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    passage = passage.strip()
    if not passage:
        return {"questions": [], "error": "Please enter a topic or passage."}

    prompt = f"""
Create exactly 3 multiple-choice questions from the educational passage below.

Return ONLY valid JSON. Do not use Markdown fences.

Required format:
{{
  "questions": [
    {{
      "question": "Question text",
      "options": ["A", "B", "C", "D"],
      "correct_answer": "A"
    }}
  ]
}}

Rules:
- Exactly 3 questions.
- Exactly 4 options per question.
- correct_answer must exactly match one option.
- Questions must be answerable from the passage.
- Make distractors plausible.

Passage:
{passage}
"""

    try:
        raw = generate_text(prompt)
        data = json.loads(clean_json_block(raw))
        questions = data.get("questions", [])

        if len(questions) != 3:
            raise ValueError("The model did not return exactly 3 questions.")

        for q in questions:
            if len(q.get("options", [])) != 4:
                raise ValueError("Each question must contain exactly 4 options.")
            if q.get("correct_answer") not in q["options"]:
                raise ValueError("correct_answer must match one of the options.")

        return {"questions": questions}
    except Exception as exc:
        return {"questions": [], "error": f"Quiz generation failed: {exc}"}
