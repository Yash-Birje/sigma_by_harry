from services.groq_client import run_prompt
MAX_CHARS = 3000
def analyze(text: str) -> dict:
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]
    summary_prompt = (
        "Summarize the following article in exactly 5 concise bullet points. "
        "Do not add any commentary.\n\n"
        f"{text}"
    )
    topics_prompt = (
        "Extract exactly 5 key topic tags from the following article. "
        "Return them as a comma-separated list. "
        "Do not explain nor add reasoning.\n\n"
        f"{text}"
    )
    sentiment_prompt = (
        "Classify the overall sentiment of the following article as "
        "Positive, Negative, or Neutral. "
        "Respond with only one word.\n\n"
        f"{text}"
    )
    summary = run_prompt(summary_prompt)
    topics = run_prompt(topics_prompt)
    sentiment = run_prompt(sentiment_prompt)

    return {
        "summary": summary,
        "topics": topics,
        "sentiment": sentiment
    }