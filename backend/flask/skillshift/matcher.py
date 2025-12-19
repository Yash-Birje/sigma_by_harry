from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def calculate_match(resume_text: str, job_text: str) -> float:
    resume_text = preprocess(resume_text)
    job_text = preprocess(job_text)

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf = vectorizer.fit_transform([resume_text, job_text])

    # print("FEATURES:", vectorizer.get_feature_names_out())

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(float(score), 4)
