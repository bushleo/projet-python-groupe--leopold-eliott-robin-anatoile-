import csv
import matplotlib.pyplot as plt

# --- Fonction pour charger dates et taux depuis un CSV ---
def charger(chemin):
    dates = []
    taux = []
    with open(chemin, newline="") as f:
        lecteur = csv.reader(f)
        next(lecteur)                      # sauter l'en-tete
        for ligne in lecteur:
            dates.append(ligne[0])         # colonne date
            taux.append(float(ligne[2]))   # colonne taux
    return dates, taux


# =====================================================================
# C.1 : UNE PREMIERE COURBE (evolution du dollar)
# =====================================================================

dates, taux = charger("donnees/taux_EUR_USD.csv")

# On cree une figure et des axes
fig, ax = plt.subplots(figsize=(10, 5))

# On trace la courbe : les dates en x, les taux en y
ax.plot(dates, taux)

# On ajoute un titre et des legendes d'axes
ax.set_title("Evolution du taux EUR/USD")
ax.set_xlabel("Date")
ax.set_ylabel("Taux")

# Il y a trop de dates pour l'axe x : on n'affiche qu'une date sur 20
ax.set_xticks(dates[::20])
plt.xticks(rotation=45)     # on incline les dates pour qu'elles soient lisibles

# On ajuste la mise en page et on sauvegarde en PNG
plt.tight_layout()
plt.savefig("courbe_usd.png")
print("Graphique sauvegarde dans courbe_usd.png")


# =====================================================================
# C.2 : PLUSIEURS GRAPHIQUES
# =====================================================================

# On charge aussi le GBP
dates_gbp, taux_gbp = charger("donnees/taux_EUR_GBP.csv")


# --- 1) Comparer les deux devises sur un meme graphique ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, taux, label="USD")          # 1re courbe
ax.plot(dates_gbp, taux_gbp, label="GBP")  # 2e courbe
ax.set_title("Comparaison EUR/USD et EUR/GBP")
ax.set_xlabel("Date")
ax.set_ylabel("Taux")
ax.set_xticks(dates[::20])
plt.xticks(rotation=45)
ax.legend()                                # affiche la legende (USD / GBP)
plt.tight_layout()
plt.savefig("comparaison.png")
print("Graphique sauvegarde dans comparaison.png")


# --- 2) Histogramme des variations quotidiennes de l'USD ---
# On calcule les variations jour a jour (taux du jour - taux de la veille)
variations = [taux[i] - taux[i-1] for i in range(1, len(taux))]

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(variations, bins=20)               # hist = histogramme
ax.set_title("Distribution des variations quotidiennes (USD)")
ax.set_xlabel("Variation")
ax.set_ylabel("Nombre de jours")
plt.tight_layout()
plt.savefig("histogramme.png")
print("Graphique sauvegarde dans histogramme.png")


# --- 3) Deux graphiques cote a cote (subplots) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))  # 1 ligne, 2 colonnes

ax1.plot(dates, taux)                      # graphique de gauche
ax1.set_title("USD")
ax1.set_xticks(dates[::30])

ax2.plot(dates_gbp, taux_gbp)              # graphique de droite
ax2.set_title("GBP")
ax2.set_xticks(dates_gbp[::30])

plt.tight_layout()
plt.savefig("cote_a_cote.png")
print("Graphique sauvegarde dans cote_a_cote.png")