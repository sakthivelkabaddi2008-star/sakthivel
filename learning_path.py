from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        return "Please enter a topic for a learning path."

    prompt = f"""
Create a personalized learning path for the topic: {topic}

Organize it from beginner to advanced.
Include:
1. Prerequisites
2. Beginner concepts
3. Intermediate concepts
4. Advanced concepts
5. A practical project or practice activity
6. A suggested timeline
7. Useful learning resources such as videos, articles, or books

Keep the plan structured, realistic, and easy for a student to follow.
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to create a learning path right now: {exc}"
