from newspaper import Article

def fetch_article_text(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()

    text = article.text.strip()

    if len(text) < 500:
        raise ValueError("Failed to extract meaningful article text")

    return text