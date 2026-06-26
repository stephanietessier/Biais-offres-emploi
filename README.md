# Analyse des biais dans les offres d'emploi 👩‍💼⚖️🤖

Projet **AI for Good / égalité femmes-hommes** avec données imaginées, prêt pour **GitHub** et **Google Colab**.

## Objectif

Analyser automatiquement des offres d'emploi fictives pour détecter certains signaux de biais possibles dans le langage.

Le projet peut aider à repérer :

- langage trop masculin codé ;
- langage trop agressif ou exclusif ;
- exigences excessives ;
- manque d'inclusion ;
- termes qui peuvent décourager certaines candidates ou certains candidats ;
- score global de biais ;
- recommandations de réécriture inclusive.

> ⚠️ Les données sont fictives. Ce projet est pédagogique et ne doit pas être utilisé seul pour prendre des décisions RH réelles.

## Fonctionnalités

- Génération d'un dataset fictif d'offres d'emploi.
- Détection de mots potentiellement biaisés.
- Classification du risque de biais : `faible`, `modéré`, `élevé`.
- Modèle NLP avec TF-IDF + Logistic Regression.
- Score de biais explicable.
- Suggestions de réécriture.
- Notebook Google Colab inclus.
- Structure prête pour GitHub.

## Structure

```text
job_posting_bias_analysis_project/
├── data/
│   └── job_postings_bias_fake_dataset.csv
├── notebooks/
│   └── job_posting_bias_analysis_colab.ipynb
├── outputs/
├── src/
│   ├── generate_fake_data.py
│   ├── bias_rules.py
│   ├── train_model.py
│   ├── analyze_sample.py
│   └── utils.py
├── requirements.txt
├── README.md
└── .github/workflows/python-check.yml
```

## Installation

```bash
pip install -r requirements.txt
```

## Exécution locale

```bash
python src/generate_fake_data.py
python src/train_model.py
python src/analyze_sample.py
```

## Colab

Ouvre :

```text
notebooks/job_posting_bias_analysis_colab.ipynb
```

Puis exécute les cellules.

## Exemple

Texte :

```text
Nous cherchons un rockstar developer agressif, dominant, capable de travailler sous pression extrême.
```

Sortie possible :

```text
Risque de biais : élevé
Mots détectés : rockstar, agressif, dominant, pression extrême
Suggestion : remplacer par un langage plus neutre et inclusif.
```

## Limites importantes

Ce projet détecte des signaux linguistiques simples. Il ne prouve pas qu'une entreprise discrimine.  
Pour un usage réel, il faut :

- audit humain ;
- contexte légal local ;
- validation avec spécialistes RH ;
- données réelles diversifiées ;
- tests d'équité approfondis.

## Idées d'amélioration

- Ajouter un dashboard Streamlit.
- Ajouter un modèle BERT multilingue.
- Ajouter détection de biais envers l'âge, handicap, origine, parentalité.
- Ajouter réécriture automatique inclusive.
- Ajouter analyse comparative de plusieurs entreprises.
- Ajouter une API FastAPI.

## Licence

MIT
