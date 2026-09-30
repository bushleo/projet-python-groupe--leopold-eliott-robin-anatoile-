import csv

# --- On charge les donnees (dates et taux) depuis le CSV ---
dates = []
taux = []
with open("donnees/taux_EUR_USD.csv", newline="") as f:
    lecteur = csv.reader(f)
    next(lecteur)                 # sauter l'en-tete
    for ligne in lecteur:
        dates.append(ligne[0])    # colonne date
        taux.append(float(ligne[2]))  # colonne taux -> nombre


# =====================================================================
# A.1 : LES COMPREHENSIONS
# =====================================================================
print("--- A.1 : Comprehensions ---")

# Compréhension de liste : les taux en pourcentage (x100)
taux_pourcent = [t * 100 for t in taux]
print("5 premiers taux x100 :", taux_pourcent[:5])

# Compréhension de liste avec condition : seulement les taux > 1.18
taux_eleves = [t for t in taux if t > 1.18]
print("Nombre de taux > 1.18 :", len(taux_eleves))

# Compréhension de dictionnaire : associer chaque date a son taux
dico_taux = {d: t for d, t in zip(dates, taux)}
print("Taux du 2026-01-02 :", dico_taux["2026-01-02"])


# =====================================================================
# A.2 : enumerate, zip, sorted
# =====================================================================
print("\n--- A.2 : enumerate, zip, sorted ---")

# enumerate : indice + valeur en meme temps
for i, t in enumerate(taux[:3]):
    print("indice", i, "-> taux", t)

# zip : associer deux listes (dates et taux)
for d, t in list(zip(dates, taux))[:3]:
    print(d, "->", t)

# sorted avec key : trier les dates selon leur taux (du plus petit au plus grand)
paires = list(zip(dates, taux))
paires_triees = sorted(paires, key=lambda couple: couple[1])
print("Date du taux le plus bas :", paires_triees[0])
print("Date du taux le plus haut :", paires_triees[-1])


# =====================================================================
# A.3 : f-strings, lambda, map/filter
# =====================================================================
print("\n--- A.3 : f-strings, lambda, map/filter ---")

# f-string : afficher un nombre a 2 decimales
moyenne = sum(taux) / len(taux)
print(f"La moyenne est de {moyenne:.2f}")
print(f"Le premier taux est {taux[0]:.4f} le {dates[0]}")

# lambda + map : appliquer une fonction a toute la liste
taux_arrondis = list(map(lambda t: round(t, 2), taux))
print("5 premiers taux arrondis :", taux_arrondis[:5])

# lambda + filter : garder seulement certaines valeurs
taux_bas = list(filter(lambda t: t < 1.14, taux))
print("Nombre de taux < 1.14 :", len(taux_bas))