import pandas as pd
import spacy
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from imblearn.over_sampling import SMOTE

filepath = "./dataset/spam.csv"
df = pd.read_csv(filepath)

encoder = LabelEncoder()

y = encoder.fit_transform(df['Category'])

nlp = spacy.load('en_core_web_sm')

def preprocessing(sent):
    doc = nlp(sent)
    filtered_data = []
    for token in doc:
        if token.is_stop:
            continue
        filtered_data.append(token.lemma_)
    return " ".join(filtered_data)

X = df['Message'].apply(preprocessing)

vect = TfidfVectorizer()
X = vect.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

smote = SMOTE(sampling_strategy='minority')
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

model = LogisticRegression()
model.fit(X_train_res, y_train_res)

preds = model.predict(X_test)
print(classification_report(y_test, preds))

joblib.dump(vect, 'tfidf.pkl')
joblib.dump(model, 'model.pkl')
joblib.dump(encoder, 'label_encoder.pkl')