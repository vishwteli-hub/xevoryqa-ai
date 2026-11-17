
print("1. Script started", flush=True)

import pandas as pd
print("2. Pandas imported", flush=True)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
print("3. Scikit-learn imported", flush=True)

print("4. Loading dataset...", flush=True)

data = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

print("5. Dataset loaded:", len(data), "messages", flush=True)

X = data["message"]
y = data["label"]

print("6. Splitting dataset...", flush=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("7. Dataset split completed", flush=True)

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

print("8. Converting text...", flush=True)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

print("9. Text conversion completed", flush=True)

model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

print("10. Training model...", flush=True)

model.fit(X_train_vectorized, y_train)

print("11. Model training completed", flush=True)

predictions = model.predict(X_test_vectorized)

print("12. Predictions completed", flush=True)

print("\n========== MODEL EVALUATION ==========")

print(
    "\nAccuracy:",
    f"{accuracy_score(y_test, predictions) * 100:.2f}%"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions,
        labels=["ham", "spam"],
        target_names=["Legitimate", "Spam"]
    )
)

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        predictions,
        labels=["ham", "spam"]
    )
)

print("\n========== EVALUATION COMPLETE ==========")
