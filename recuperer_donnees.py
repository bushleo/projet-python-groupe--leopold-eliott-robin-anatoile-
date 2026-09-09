"""Récupère les taux de change de la BCE et fabrique le fichier CSV."""

import csv
import json
import urllib.request
from pathlib import Path

URL = "https://api.frankfurter.app/2026-01-01..2026-09-01?from=EUR&to=USD"

# On appelle l'API et on lit la réponse
requete = urllib.request.Request(URL, headers={"User-Agent": "projet-python-bfa1"})

with urllib.request.urlopen(requete) as reponse:
    texte = reponse.read().decode("utf-8")

donnees = json.loads(texte)

# On sauvegarde la réponse brute dans cache/
Path("cache").mkdir(exist_ok=True)
Path("cache/reponse_serie.json").write_text(texte, encoding="utf-8")
print("Réponse brute enregistrée dans cache/reponse_serie.json")

# On écrit le CSV dans donnees/
Path("donnees").mkdir(exist_ok=True)
with open("donnees/taux.csv", "w", encoding="utf-8", newline="") as f:
    ecrivain = csv.writer(f)
    ecrivain.writerow(["date", "taux"])
    for date in sorted(donnees["rates"]):
        ecrivain.writerow([date, donnees["rates"][date]["USD"]])

print(f"CSV créé : {len(donnees['rates'])} lignes")