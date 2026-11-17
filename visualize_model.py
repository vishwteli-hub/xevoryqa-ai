
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# Load dataset
data = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

X = data["message"]
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Convert text into numerical features
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train_vectorized, y_train)

# Predictions
predictions = model.predict(X_test_vectorized)

# Calculate metrics
accuracy = accuracy_score(y_test, predictions)

report = classification_report(
    y_test,
    predictions,
    labels=["ham", "spam"],
    target_names=["Legitimate", "Spam"],
    output_dict=True
)

# Print evaluation summary
print("\n========== MODEL PERFORMANCE ==========")
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Spam Precision: {report['Spam']['precision'] * 100:.2f}%")
print(f"Spam Recall: {report['Spam']['recall'] * 100:.2f}%")
print(f"Spam F1-score: {report['Spam']['f1-score'] * 100:.2f}%")

# Create dashboard
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Chart 1: Confusion Matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=["ham", "spam"]
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Legitimate", "Spam"]
)

display.plot(
    ax=axes[0],
    cmap="Blues",
    colorbar=False
)

axes[0].set_title("Confusion Matrix")

# Chart 2: Performance Metrics
metrics = [
    report["Spam"]["precision"],
    report["Spam"]["recall"],
    report["Spam"]["f1-score"]
]

metric_names = ["Precision", "Recall", "F1-score"]

axes[1].bar(metric_names, metrics)
axes[1].set_ylim(0, 1)
axes[1].set_ylabel("Score")
axes[1].set_title("Spam Detection Performance")
axes[1].grid(axis="y", alpha=0.3)

for index, value in enumerate(metrics):
    axes[1].text(
        index,
        value + 0.02,
        f"{value:.1%}",
        ha="center"
    )

# Overall dashboard title
fig.suptitle(
    f"ScamShield AI - Model Evaluation | Accuracy: {accuracy:.2%}",
    fontsize=14
)

plt.tight_layout()

# Save dashboard
plt.savefig(
    "model_performance.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard saved as model_performance.png")

# Display dashboard
plt.show()
