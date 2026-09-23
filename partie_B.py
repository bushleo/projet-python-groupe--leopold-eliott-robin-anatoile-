import pandas as pd

# --- Charger le CSV ---
df = pd.read_csv("donnees/taux_EUR_USD.csv")

# --- Transformer la colonne "date" en vraie date ---
df["date"] = pd.to_datetime(df["date"])

# --- Mettre la date comme index (l'etiquette de chaque ligne) ---
df = df.set_index("date")

print("Nombre de lignes AVANT de combler les trous :", len(df))


# --- B.1 : combler les jours manquants (forward-fill) ---
# On cree un calendrier continu de tous les jours ouvres (lundi a vendredi)
calendrier = pd.date_range(start=df.index.min(),
                           end=df.index.max(),
                           freq="B")   # "B" = Business days (jours ouvres)

# On reindexe le tableau sur ce calendrier complet
df = df.reindex(calendrier)

print("Nombre de lignes APRES avoir cree le calendrier :", len(df))
print("\nJours manquants (NaN) avant forward-fill :", df["taux"].isna().sum())

# forward-fill : on recopie la derniere valeur connue dans les trous
df["taux"] = df["taux"].ffill()

print("Jours manquants (NaN) apres forward-fill :", df["taux"].isna().sum())

print("\nLes 10 premieres lignes apres nettoyage :")
print(df[["taux"]].head(10))


# =====================================================================
# B.2 : ANALYSER
# =====================================================================

# --- 1) Variation en % sur toute la periode ---
premier_taux = df["taux"].iloc[0]    # tout premier taux
dernier_taux = df["taux"].iloc[-1]   # tout dernier taux
variation = (dernier_taux - premier_taux) / premier_taux * 100

print("\n--- Variation sur la periode ---")
print("Premier taux :", premier_taux)
print("Dernier taux :", dernier_taux)
print("Variation    :", round(variation, 2), "%")


# --- 2) Moyenne mobile sur 7 jours ---
df["moyenne_mobile"] = df["taux"].rolling(window=7).mean()

print("\n--- Moyenne mobile (7 jours) ---")
print(df[["taux", "moyenne_mobile"]].head(10))


# --- 3) R",echantillonner en donnees mensuelles ---
mensuel = df["taux"].resample("ME").mean()

print("\n--- Moyenne par mois (resample) ---")
print(mensuel)