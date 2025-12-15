from flask import Flask
from services.article_fetcher import fetch_article_text
from services.analyzer import summarize

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://en.wikipedia.org/wiki/Machine_learning"
    try:
        text = fetch_article_text(url)
        summary = summarize(text)
        return f"<pre>{summary}</pre>"  # show first 1000 chars only
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
