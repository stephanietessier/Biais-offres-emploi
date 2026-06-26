from joblib import load
from utils import OUTPUT_DIR
from bias_rules import rule_based_bias_score, rewrite_suggestions

MODEL_PATH = OUTPUT_DIR / "job_bias_model.joblib"

def analyze_text(text):
    model = load(MODEL_PATH)
    ml_prediction = model.predict([text])[0]
    probabilities = dict(zip(model.classes_, model.predict_proba([text])[0]))
    rule_result = rule_based_bias_score(text)
    suggestions = rewrite_suggestions(text)

    return {
        "ml_prediction": ml_prediction,
        "probabilities": probabilities,
        "rule_result": rule_result,
        "suggestions": suggestions,
    }

def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Lance d'abord : python src/train_model.py")

    sample = (
        "Nous cherchons un rockstar developer agressif, dominant et compétitif. "
        "La personne doit être disponible en tout temps, travailler sous pression extrême "
        "et accepter des heures illimitées."
    )

    result = analyze_text(sample)

    print("Offre analysée :")
    print(sample)

    print("\\nPrédiction ML :", result["ml_prediction"])
    print("Score règles :", result["rule_result"]["score"])
    print("Risque règles :", result["rule_result"]["risk"])
    print("Mots masculins codés :", result["rule_result"]["masculine_coded_terms"])
    print("Termes exclusifs :", result["rule_result"]["exclusionary_terms"])

    print("\\nSuggestions :")
    for suggestion in result["suggestions"]:
        print("-", suggestion)

if __name__ == "__main__":
    main()
