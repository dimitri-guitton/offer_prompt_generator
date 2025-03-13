#!/usr/bin/env python3
import json

def load_profile_from_json(file_path):
    """
    Charge le profil utilisateur à partir d'un fichier JSON.
    """
    with open(file_path, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
    return data


def build_prompt(profile_data, offre_text, extra_info=None):
    """
    Construit un prompt en injectant les informations du profil dans un template prédéfini.

    Args:
        profile_data (dict): Données du profil (chargées depuis le JSON).
        offre_text (str): Texte de l'offre d'emploi.

    Returns:
        str: Le prompt complet.
    """
    profil = profile_data.get("profil", {})
    experience = profile_data.get("experience", [])
    formation = profile_data.get("formation", [])
    competences = profile_data.get("competences", [])
    projets = profile_data.get("projets", [])
    certifications = profile_data.get("certifications", [])
    prompt = ""

    # Construction du prompt avec le profil utilisateur
    prompt = "=== Context ===\n"
    prompt = "=== Profil de l'utilisateur ===\n"
    prompt += f"Nom : {profil.get('nom', 'N/A')}\n"
    prompt += f"Titre : {profil.get('titre', 'N/A')}\n"
    prompt += f"Localisation : {profil.get('localisation', 'N/A')}\n"
    contact = profil.get("contact", {})
    prompt += f"Email : {contact.get('email', 'N/A')}\n"
    prompt += f"Téléphone : {contact.get('telephone', 'N/A')}\n"
    prompt += f"Site Web : {contact.get('site_web', 'N/A')}\n"
    prompt += f"Résumé : {profil.get('resume', 'N/A')}\n\n"

    prompt += "=== Expériences professionnelles ===\n"
    for exp in experience:
        prompt += f"- Poste : {exp.get('poste', 'N/A')} chez {exp.get('entreprise', 'N/A')}\n"
        prompt += f"  Durée : {exp.get('date_debut', 'N/A')} à {exp.get('date_fin', 'N/A')}\n"
        prompt += f"  Description : {exp.get('description', 'N/A')}\n"
    prompt += "\n=== Formations ===\n"
    for f in formation:
        prompt += f"- {f.get('diplome', 'N/A')} à {f.get('etablissement', 'N/A')} ({f.get('annee', 'N/A')})\n"
    prompt += "\n=== Compétences ===\n"
    prompt += ", ".join(competences) + "\n\n"

    prompt += "=== Projets réalisés ===\n"
    for projet in projets:
        prompt += f"- {projet.get('nom', 'N/A')}:\n"
        prompt += f"  Description : {projet.get('description', 'N/A')}\n"
        prompt += f"  Technologies : {', '.join(projet.get('technologies', []))}\n"
        lien = projet.get("lien", "")
        if lien:
            prompt += f"  Lien : {lien}\n"
    prompt += "\n=== Certifications ===\n"
    for cert in certifications:
        prompt += f"- {cert.get('titre', 'N/A')} par {cert.get('organisme', 'N/A')} ({cert.get('date_obtention', 'N/A')})\n"

    prompt += "=== Fin du profil ===\n"

    prompt += "\n=== Offre d'emploi à répondre ===\n"
    prompt += offre_text + "\n"
    prompt += "=== Fin de l'offre d'emploi ===\n"


    prompt += "Je voudrait que tu me positionne sur cette offre d'emploi en tant que développeur freelance. Génère moi une réponse à cette offre d'emploi en utilisant les informations de mon profil ci-dessus.\n"

    if extra_info:
        prompt += f"\n=== Informations supplémentaires ===\n"
        prompt += extra_info + "\n"
        prompt += "=== Fin des informations supplémentaires ===\n"

    return prompt

