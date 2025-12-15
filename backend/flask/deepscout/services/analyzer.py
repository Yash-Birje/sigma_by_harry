from services.groq_client import run_prompt

def summarize(text: str) -> str:
    prompt = (
        "Summarize the following article in exactly 5 concise bullet points. "
        "Do not add any commentary.\n\n"
        f"{text}"
    )
    return run_prompt(prompt)