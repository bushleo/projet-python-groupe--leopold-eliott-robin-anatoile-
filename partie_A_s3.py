import pandas as pd

# --- A.1 : charger le CSV dans un DataFrame ---
df = pd.read_csv("donnees/taux_EUR_USD.csv")

print("Les 5 premieres lignes :")
print(df.head())

print("\nInfos statistiques (describe) :")
print(df.describe())

print("\nType de chaque colonne (dtypes) :")
print(df.dtypes)


# --- A.2 : selectionner une colonne (une Series) ---
colonne_taux = df["taux"]
print("\nLa colonne taux (une Series), 5 premieres valeurs :")
print(colonne_taux.head())

# Filtrer : garder seulement les lignes ou le taux depasse 1.18
taux_eleves = df[df["taux"] > 1.18]
print("\nLes jours ou le taux depasse 1.18 :")
print(taux_eleves)

# Moyenne, minimum, maximum (en une ligne chacun)
print("\nMoyenne :", df["taux"].mean())
print("Minimum :", df["taux"].min())
print("Maximum :", df["taux"].max())