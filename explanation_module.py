import os
from functools import lru_cache

from gemini_client import generate_text


@lru_cache(maxsize=1)
def _local_pipeline():
    from transformers import pipeline

    model_name = os.getenv(
        "LOCAL_EXPLANATION_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M",
    )
    return pipeline(
        "text2text-generation",
        model=model_name,
        tokenizer=model_name,
        device=-1,
    )


def explain_topic(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        return "Please enter a topic to explain."

    prompt = (
        "Explain the following educational topic for a beginner. "
        "Use simple language, a short example, and 3 key points. "
        f"Topic: {topic}"
    )

    try:
        result = _local_pipeline()(prompt, max_new_tokens=220, do_sample=False)
        return result[0]["generated_text"].strip()
    except Exception as local_exc:
        # Keeps the application usable if the local model is not installed or
        # cannot run on the current machine.
        try:
            return generate_text(prompt)
        except Exception as gemini_exc:
            return (
                "Explanation service is unavailable. "
                f"Local model error: {local_exc}. Gemini error: {gemini_exc}"
            )
