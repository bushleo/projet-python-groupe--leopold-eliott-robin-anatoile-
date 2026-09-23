import pandas as pd
import numpy as np

# --- Charger le CSV et recuperer la colonne des taux ---
df = pd.read_csv("donnees/taux_EUR_USD.csv")

# =====================================================================
# D.1 : DU DATAFRAME AU TABLEAU NUMPY
# =====================================================================

# Convertir la colonne "taux" en tableau numpy
taux = df["taux"].to_numpy()

print("Type de l'objet :", type(taux))
print("Les 5 premieres valeurs :", taux[:5])

# Calculs vectorises (sans boucle)
print("\n--- Calculs numpy (sans boucle) ---")
print("Moyenne     :", np.mean(taux))
print("Ecart-type  :", np.std(taux))
print("Minimum     :", np.min(taux))
print("Maximum     :", np.max(taux))

# Variations jour a jour (difference entre chaque jour et le precedent)
variations = np.diff(taux)
print("\nLes 5 premieres variations jour a jour :", variations[:5])


# =====================================================================
# D.2 : COMPRENDRE numpy (dtype et broadcasting)
# =====================================================================

# Le dtype = le type des elements du tableau
print("\n--- dtype ---")
print("Type des elements :", taux.dtype)

# Broadcasting = operation entre un tableau et un simple nombre
print("\n--- broadcasting ---")
taux_en_pourcentage = taux * 100   # multiplie CHAQUE valeur par 100
print("5 premieres valeurs x 100 :", taux_en_pourcentage[:5])


# =====================================================================
# D.3 : APERCU DE POLARS (alternative a pandas)
# =====================================================================
import polars as pl
import time

# --- Charger le meme CSV, mais avec polars ---
df_pl = pl.read_csv("donnees/taux_EUR_USD.csv")

print("\n--- polars : les 5 premieres lignes ---")
print(df_pl.head())

# --- Quelques calculs en polars ---
print("\n--- polars : calculs ---")
moyenne_pl = df_pl["taux"].mean()
mini_pl = df_pl["taux"].min()
maxi_pl = df_pl["taux"].max()
print("Moyenne :", moyenne_pl)
print("Minimum :", mini_pl)
print("Maximum :", maxi_pl)

# --- Comparaison de vitesse pandas vs polars ---
print("\n--- Comparaison du temps de calcul de la moyenne ---")

debut = time.time()
for _ in range(1000):
    df["taux"].mean()          # pandas, 1000 fois
temps_pandas = time.time() - debut

debut = time.time()
for _ in range(1000):
    df_pl["taux"].mean()       # polars, 1000 fois
temps_polars = time.time() - debut

print("Temps pandas :", round(temps_pandas, 4), "secondes")
print("Temps polars :", round(temps_polars, 4), "secondes")