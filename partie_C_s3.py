import pandas as pd

# =====================================================================
# C.1 : REUNIR LES DEUX DEVISES (USD et GBP)
# =====================================================================

# --- Charger les deux fichiers, un par devise ---
usd = pd.read_csv("donnees/taux_EUR_USD.csv")
gbp = pd.read_csv("donnees/taux_EUR_GBP.csv")

print("Tableau USD (5 premieres lignes) :")
print(usd.head())
print("\nTableau GBP (5 premieres lignes) :")
print(gbp.head())

# --- Garder seulement les colonnes date et taux, et renommer taux ---
usd = usd[["date", "taux"]].rename(columns={"taux": "USD"})
gbp = gbp[["date", "taux"]].rename(columns={"taux": "GBP"})

# --- La jointure : coller les deux tableaux sur la colonne "date" ---
ensemble = pd.merge(usd, gbp, on="date", how="inner")

print("\n--- Les deux devises reunies (merge sur la date) ---")
print(ensemble.head(10))

print("\nNombre de lignes :")
print("USD seul :", len(usd))
print("GBP seul :", len(gbp))
print("Apres merge :", len(ensemble))


# =====================================================================
# C.2 : LES 4 TYPES DE JOINTURE
# =====================================================================

# Deux petites tables avec des cles partiellement communes
gauche = pd.DataFrame({"cle": [1, 2], "valeur_gauche": ["G1", "G2"]})
droite = pd.DataFrame({"cle": [2, 3], "valeur_droite": ["D2", "D3"]})

print("\nTable de GAUCHE :")
print(gauche)
print("\nTable de DROITE :")
print(droite)

print("\n--- INNER (seulement les cles communes) ---")
print(pd.merge(gauche, droite, on="cle", how="inner"))

print("\n--- LEFT (toutes les cles de gauche) ---")
print(pd.merge(gauche, droite, on="cle", how="left"))

print("\n--- RIGHT (toutes les cles de droite) ---")
print(pd.merge(gauche, droite, on="cle", how="right"))

print("\n--- OUTER (toutes les cles des deux) ---")
print(pd.merge(gauche, droite, on="cle", how="outer"))



# =====================================================================
# C.3 : merge, join ou concat ?
# =====================================================================

# Deux petites tables pour illustrer
table1 = pd.DataFrame({"jour": ["lun", "mar"], "ventes": [10, 20]})
table2 = pd.DataFrame({"jour": ["mer", "jeu"], "ventes": [30, 40]})

# concat : empiler les unes SOUS les autres (rallonger)
empile = pd.concat([table1, table2], ignore_index=True)
print("\n--- CONCAT : empiler (ajouter des lignes) ---")
print(empile)

# Rappel merge : apparier sur une cle commune
prix = pd.DataFrame({"jour": ["lun", "mar"], "prix": [5, 6]})
apparie = pd.merge(table1, prix, on="jour", how="inner")
print("\n--- MERGE : apparier sur la cle 'jour' (ajouter des colonnes) ---")
print(apparie)