MASCULINE_CODED_WORDS = [
    "agressif", "dominant", "compétitif", "rockstar", "ninja", "guerrier",
    "ambitieux à l'extrême", "fonceur", "leader né", "impitoyable",
    "sous pression extrême", "performeur", "conquérant"
]

EXCLUSIONARY_PHRASES = [
    "jeune diplômé", "sans contraintes familiales", "disponible en tout temps",
    "doit être natif", "culture très masculine", "heures illimitées",
    "pas de télétravail possible", "présence obligatoire soir et weekend"
]

INCLUSIVE_PHRASES = [
    "candidatures de tous horizons", "environnement inclusif",
    "horaire flexible", "équilibre travail vie personnelle",
    "accommodements raisonnables", "nous encourageons les femmes à postuler",
    "équipe diversifiée", "langage inclusif", "télétravail possible"
]

REPLACEMENTS = {
    "rockstar": "développeuse ou développeur expérimenté(e)",
    "ninja": "spécialiste",
    "guerrier": "personne engagée",
    "agressif": "proactif",
    "dominant": "capable de coordonner",
    "impitoyable": "rigoureux",
    "sous pression extrême": "dans un environnement dynamique",
    "disponible en tout temps": "avec disponibilité raisonnable",
    "heures illimitées": "horaire clair et soutenable",
    "sans contraintes familiales": "avec disponibilité compatible avec le poste",
}

def count_terms(text, terms):
    text_lower = text.lower()
    return [term for term in terms if term.lower() in text_lower]

def rule_based_bias_score(text):
    masculine_hits = count_terms(text, MASCULINE_CODED_WORDS)
    exclusion_hits = count_terms(text, EXCLUSIONARY_PHRASES)
    inclusive_hits = count_terms(text, INCLUSIVE_PHRASES)

    score = 0
    score += len(masculine_hits) * 2
    score += len(exclusion_hits) * 3
    score -= len(inclusive_hits) * 2
    score = max(0, score)

    if score >= 9:
        risk = "élevé"
    elif score >= 4:
        risk = "modéré"
    else:
        risk = "faible"

    return {
        "score": score,
        "risk": risk,
        "masculine_coded_terms": masculine_hits,
        "exclusionary_terms": exclusion_hits,
        "inclusive_terms": inclusive_hits,
    }

def rewrite_suggestions(text):
    suggestions = []
    lower = text.lower()

    for bad, better in REPLACEMENTS.items():
        if bad in lower:
            suggestions.append(f"Remplacer « {bad} » par « {better} ».")

    if "horaire flexible" not in lower and "flexible" not in lower:
        suggestions.append("Ajouter une mention d'horaire flexible lorsque possible.")

    if "candidatures de tous horizons" not in lower and "inclusif" not in lower:
        suggestions.append("Ajouter une phrase encourageant les candidatures de tous horizons.")

    if not suggestions:
        suggestions.append("Le texte semble relativement inclusif selon les règles simples du projet.")

    return suggestions
