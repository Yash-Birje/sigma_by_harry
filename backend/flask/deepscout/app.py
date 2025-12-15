from flask import Flask
from services.article_fetcher import fetch_article_text

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://example.com"
    try:
        text = fetch_article_text(url)
        return text[:1000]  # show first 1000 chars only
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
