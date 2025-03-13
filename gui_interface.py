#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, scrolledtext

from prompt_generator import build_prompt, load_profile_from_json


def analyser_offre():
    """
    Récupère le texte de l'offre, construit le prompt en combinant avec le profil,
    appelle l'API et affiche la réponse.
    """
    offre_text = txt_offre.get("1.0", tk.END).strip()
    info_sup_text = txt_info_sup.get("1.0", tk.END).strip()
    if not offre_text:
        messagebox.showwarning("Attention", "Veuillez saisir le texte de l'offre d'emploi.")
        return

    try:
        profile_data = load_profile_from_json("profile.json")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de charger le profil : {e}")
        return

    prompt = build_prompt(profile_data, offre_text, info_sup_text)

    # Affichage du prompt généré
    txt_prompt.config(state = "normal")
    txt_prompt.delete("1.0", tk.END)
    txt_prompt.insert(tk.END, prompt)
    txt_prompt.config(state = "disabled")


# Création de l'interface graphique
fenetre = tk.Tk()
fenetre.title("Analyse d'Offre d'Emploi")

# Zone pour saisir l'offre d'emploi
frame_offre = tk.LabelFrame(fenetre, text = "Saisissez l'offre d'emploi")
frame_offre.pack(fill = "both", expand = True, padx = 10, pady = 5)
txt_offre = scrolledtext.ScrolledText(frame_offre, wrap = tk.WORD, width = 80, height = 10)
txt_offre.pack(padx = 5, pady = 5)
txt_offre.config(state = "normal")

# Zone pour saisir des infos supplémentaires
frame_info_sup = tk.LabelFrame(fenetre, text = "Saisissez des informations supplémentaires")
frame_info_sup.pack(fill = "both", expand = True, padx = 10, pady = 5)
txt_info_sup = scrolledtext.ScrolledText(frame_info_sup, wrap = tk.WORD, width = 80, height = 10)
txt_info_sup.pack(padx = 5, pady = 5)
txt_info_sup.config(state = "normal")

# Bouton pour lancer l'analyse
btn_analyser = tk.Button(fenetre, text = "Générer le prompt", command = analyser_offre)
btn_analyser.pack(pady = 5)

# Zone pour afficher le prompt généré (lecture seule)
frame_prompt = tk.LabelFrame(fenetre, text = "Prompt généré")
frame_prompt.pack(fill = "both", expand = True, padx = 10, pady = 5)
txt_prompt = scrolledtext.ScrolledText(frame_prompt, wrap = tk.WORD, width = 80, height = 10)
txt_prompt.pack(padx = 5, pady = 5)
txt_prompt.config(state = "disabled")

fenetre.mainloop()
