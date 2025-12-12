from flask import Flask, render_template, request, jsonify
import joblib
import os
import spacy

# --- load spaCy and disable heavy components for speed ---
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner', 'textcat'])

# --- YOUR preprocessing function (must match training exactly) ---
def preprocessing(sent):
    if sent is None:
        return ""
    doc = nlp(sent)
    filtered_data = []
    for token in doc:
        # NOTE: keep exactly the same checks you used during training
        if token.is_stop:
            continue
        filtered_data.append(token.lemma_)
    return " ".join(filtered_data)

# --- Flask app and artifact loading (once at startup) ---
app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)
VECT_PATH = os.path.join(BASE_DIR, 'tfidf.pkl')
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
ENC_PATH = os.path.join(BASE_DIR, 'label_encoder.pkl')

vectorizer = joblib.load(VECT_PATH)
model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENC_PATH)  # if you want readable labels

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    confidence = None
    input_text = None

    if request.method == 'POST':
        input_text = request.form.get('message', '')
        if not input_text:
            return render_template('index.html', result="No text provided", input_text=input_text)

        cleaned = preprocessing(input_text)
        X_vec = vectorizer.transform([cleaned])   # IMPORTANT: use transform(), not fit_transform()

        pred_idx = model.predict(X_vec)[0]
        # decode to original label if you want
        try:
            pred_label = label_encoder.inverse_transform([pred_idx])[0]
        except Exception:
            pred_label = str(pred_idx)

        # if model supports probabilities
        if hasattr(model, 'predict_proba'):
            confidence = float(model.predict_proba(X_vec)[0].max())

        return render_template('index.html', result=pred_label, confidence=confidence, input_text=input_text)

    return render_template('index.html', result=None)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json(force=True)
    text = data.get('text', '')
    cleaned = preprocessing(text)
    X_vec = vectorizer.transform([cleaned])
    pred_idx = model.predict(X_vec)[0]
    try:
        pred_label = label_encoder.inverse_transform([pred_idx])[0]
    except Exception:
        pred_label = str(pred_idx)

    prob = None
    if hasattr(model, 'predict_proba'):
        prob = float(model.predict_proba(X_vec)[0].max())

    return jsonify({'prediction': pred_label, 'confidence': prob})

if __name__ == '__main__':
    app.run(debug=True)
