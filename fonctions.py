"""Séance 2 - Partie A : lecture du CSV et calculs sur les taux."""

import csv
from statistics import mean


def lire_csv(chemin):
    """Lit le CSV des taux et renvoie une liste de couples (date, taux)."""
    couples = []
    with open(chemin, "r", encoding="utf-8", newline="") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            couples.append((ligne[0], float(ligne[1])))
    return couples


def moyenne(taux):
    """Calcule la moyenne d'une liste de taux."""
    return sum(taux) / len(taux)


def minimum_maximum(taux):
    """Renvoie le taux le plus bas et le taux le plus haut."""
    return min(taux), max(taux)


donnees = lire_csv("donnees/taux.csv")
valeurs = [taux for date, taux in donnees]

print("Nombre de jours :", len(valeurs))
print("Moyenne (notre fonction) :", moyenne(valeurs))
print("Moyenne (statistics.mean) :", mean(valeurs))

mini, maxi = minimum_maximum(valeurs)
print("Minimum :", mini)
print("Maximum :", maxi)