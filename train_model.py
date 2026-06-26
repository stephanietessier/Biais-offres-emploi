import pandas as pd
import matplotlib.pyplot as plt
from joblib import dump
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from utils import DATA_DIR, OUTPUT_DIR

DATA_PATH = DATA_DIR / "job_postings_bias_fake_dataset.csv"

def train():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Lance d'abord : python src/generate_fake_data.py")

    df = pd.read_csv(DATA_PATH)

    X = df["job_posting_text"]
    y = df["bias_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True, max_features=5000)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Accuracy :", round(accuracy_score(y_test, predictions), 3))
    print(classification_report(y_test, predictions))

    model_path = OUTPUT_DIR / "job_bias_model.joblib"
    dump(model, model_path)
    print(f"Modèle sauvegardé : {model_path}")

    fig, ax = plt.subplots(figsize=(7, 5))
    ConfusionMatrixDisplay.from_predictions(y_test, predictions, ax=ax)
    plt.title("Matrice de confusion - Risque de biais")
    plt.tight_layout()
    fig_path = OUTPUT_DIR / "confusion_matrix.png"
    plt.savefig(fig_path)
    print(f"Graphique sauvegardé : {fig_path}")

if __name__ == "__main__":
    train()
