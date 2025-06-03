from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

def sentiment_classification():
    cats = ['rec.autos', 'comp.sys.mac.hardware']
    data = fetch_20newsgroups(subset='train', categories=cats, remove=('headers', 'footers', 'quotes'))
    X, y = data.data, data.target

    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    X_vec = tfidf.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_vec, y)

    preds = model.predict(X_vec)
    acc = accuracy_score(y, preds)
    print(f"Accuracy: {acc:.2f}")

    feature_names = np.array(tfidf.get_feature_names_out())
    for i, label in enumerate(data.target_names):
        top_words = feature_names[np.argsort(model.coef_[0 if i == 0 else 0] * (-1 if i == 1 else 1))[-5:]]
        print(f"Top words for '{label}': {', '.join(top_words[::-1])}")

sentiment_classification()
