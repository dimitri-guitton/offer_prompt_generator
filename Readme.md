# Analyse d'Offre d'Emploi

Ce projet est une application Python utilisant `tkinter` pour créer une interface graphique permettant générer des
prompts basés sur un profil utilisateur.

## Fonctionnalités

- Saisie de l'offre d'emploi
- Saisie d'informations supplémentaires
- Génération de prompt basé sur le profil utilisateur
- Affichage du prompt généré
- Copie du prompt généré dans le presse-papier

## Prérequis

- Python 3.x
- `tkinter` (inclus avec Python)
- `poetry`

## Installation

1. Clonez le dépôt :
    ```sh
    git clone <url-du-depot>
    cd <nom-du-repertoire>
    ```

2. Installez les dépendances :
    ```sh
    poetry install
    ```

## Utilisation

1. Lancez l'application :
    ```sh
    python gui_interface.py
    ```

2. Saisissez l'offre d'emploi et les informations supplémentaires dans les zones de texte correspondantes.

3. Cliquez sur "Générer le prompt" pour générer le prompt basé sur le profil utilisateur.

## Build

   ```sh
      make build-macos
      make build-windows
      make build-linux
   ```