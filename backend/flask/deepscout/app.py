from flask import Flask, render_template, request
from services.article_fetcher import fetch_article_text
from services.analyzer import analyze

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")
        try:
            text = fetch_article_text(url)
            result = analyze(text)
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
