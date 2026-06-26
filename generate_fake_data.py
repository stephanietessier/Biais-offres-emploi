import random
import pandas as pd
from utils import DATA_DIR
from bias_rules import rule_based_bias_score

random.seed(42)

NEUTRAL_OPENINGS = [
    "Nous recrutons une personne pour rejoindre notre équipe.",
    "Notre organisation cherche une candidate ou un candidat motivé.",
    "Nous recherchons un profil capable de collaborer avec plusieurs équipes.",
    "Ce poste vise à soutenir la croissance d'une équipe diversifiée.",
]

BIASED_OPENINGS = [
    "Nous cherchons un rockstar developer agressif et ultra compétitif.",
    "Nous voulons un guerrier capable de dominer le marché.",
    "Poste pour fonceur impitoyable capable de travailler sous pression extrême.",
    "Nous cherchons un leader né, disponible en tout temps.",
]

NEUTRAL_REQUIREMENTS = [
    "Expérience pertinente en gestion de projet ou domaine similaire.",
    "Capacité à communiquer clairement.",
    "Intérêt pour la collaboration et l'amélioration continue.",
    "Connaissance des outils numériques modernes.",
    "Capacité à résoudre des problèmes avec rigueur.",
]

BIASED_REQUIREMENTS = [
    "Doit être jeune diplômé et sans contraintes familiales.",
    "Présence obligatoire soir et weekend.",
    "Heures illimitées attendues.",
    "Culture très masculine et compétitive.",
    "Pas de télétravail possible.",
]

INCLUSIVE_SENTENCES = [
    "Nous encourageons les femmes à postuler.",
    "Nous valorisons les candidatures de tous horizons.",
    "Notre environnement inclusif soutient la diversité.",
    "Des accommodements raisonnables sont disponibles.",
    "Un horaire flexible est possible selon les besoins de l'équipe.",
    "Nous favorisons l'équilibre travail vie personnelle.",
]

JOB_TITLES = [
    "Analyste de données",
    "Développeuse ou développeur logiciel",
    "Gestionnaire de projet",
    "Spécialiste cybersécurité",
    "Scientifique des données",
    "Chargée ou chargé de produit",
    "Ingénieure ou ingénieur ML",
]

def create_posting(bias_level):
    title = random.choice(JOB_TITLES)

    if bias_level == "faible":
        parts = [
            f"Titre : {title}.",
            random.choice(NEUTRAL_OPENINGS),
            random.choice(NEUTRAL_REQUIREMENTS),
            random.choice(NEUTRAL_REQUIREMENTS),
            random.choice(INCLUSIVE_SENTENCES),
            random.choice(INCLUSIVE_SENTENCES),
        ]
    elif bias_level == "modéré":
        parts = [
            f"Titre : {title}.",
            random.choice(NEUTRAL_OPENINGS),
            random.choice(NEUTRAL_REQUIREMENTS),
            random.choice(BIASED_REQUIREMENTS),
            random.choice(INCLUSIVE_SENTENCES),
        ]
    else:
        parts = [
            f"Titre : {title}.",
            random.choice(BIASED_OPENINGS),
            random.choice(BIASED_REQUIREMENTS),
            random.choice(BIASED_REQUIREMENTS),
            "La personne devra être très compétitive et disponible en tout temps.",
        ]

    return " ".join(parts)

def generate_dataset(n=600):
    rows = []
    labels = ["faible", "modéré", "élevé"]

    for _ in range(n):
        intended_label = random.choices(labels, weights=[0.4, 0.35, 0.25])[0]
        text = create_posting(intended_label)
        rule_result = rule_based_bias_score(text)

        rows.append({
            "job_posting_text": text,
            "rule_bias_score": rule_result["score"],
            "bias_risk": rule_result["risk"],
            "detected_masculine_terms": ", ".join(rule_result["masculine_coded_terms"]),
            "detected_exclusionary_terms": ", ".join(rule_result["exclusionary_terms"]),
            "detected_inclusive_terms": ", ".join(rule_result["inclusive_terms"]),
        })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_dataset()
    output = DATA_DIR / "job_postings_bias_fake_dataset.csv"
    df.to_csv(output, index=False)
    print(f"Dataset créé : {output}")
    print(df.head())
    print(df["bias_risk"].value_counts())
