# Projet Python — Taux de change (BCE)

## Membres du groupe

- Léopold
- Eliott
- Robin
- Anatole

## Description

Projet d'analyse des taux de change de référence de la Banque centrale
européenne (API Frankfurter). Le projet couvre : récupération des données,
nettoyage, analyse avec pandas, jointures, numpy, programmation orientée
objet et visualisation avec matplotlib.

## Installation

Cloner le dépôt, puis installer les librairies nécessaires :

    pip3 install -r requirements.txt

## Utilisation

L'outil en ligne de commande s'utilise ainsi :

    python3 outil.py analyser      # affiche moyenne, min, max des taux
    python3 outil.py graphiques    # génère les graphiques

## Organisation du dépôt

- `outil.py` — outil en ligne de commande (argparse)
- `partie_A_s4.py`, `partie_B_s4.py`, `partie_C_s4.py` — scripts des parties
- `donnees/` — les fichiers CSV des taux
- `docs/` — les notes de chaque séance (réponses aux questions)
- `requirements.txt` — la liste des librairies nécessaires

## Librairies utilisées

pandas, numpy, polars, matplotlib (voir `requirements.txt`).

