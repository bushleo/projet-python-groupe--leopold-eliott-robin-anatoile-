import csv


# =====================================================================
# B.1 : NOTRE PREMIERE CLASSE
# =====================================================================

# "class" definit le modele. Par convention, le nom commence par une majuscule.
class SerieTaux:

    # __init__ est appelee automatiquement quand on cree un objet.
    # Elle remplit l'objet avec ses donnees de depart.
    # "self" = l'objet lui-meme.
    def __init__(self, devise, taux):
        self.devise = devise    # attribut : la devise (ex. "USD")
        self.taux = taux        # attribut : la liste des taux

    # Une methode = une fonction rangee dans la classe.
    # Elle prend toujours "self" en premier parametre.
    def moyenne(self):
        return sum(self.taux) / len(self.taux)

    def variation(self):
        premier = self.taux[0]
        dernier = self.taux[-1]
        return (dernier - premier) / premier * 100

    def minimum(self):
        return min(self.taux)

    def maximum(self):
        return max(self.taux)


# --- Petite fonction pour charger les taux d'un fichier ---
def charger_taux(chemin):
    taux = []
    with open(chemin, newline="") as f:
        lecteur = csv.reader(f)
        next(lecteur)                     # sauter l'en-tete
        for ligne in lecteur:
            taux.append(float(ligne[2]))  # colonne taux
    return taux


# --- On cree un OBJET (une instance) pour le dollar ---
taux_usd = charger_taux("donnees/taux_EUR_USD.csv")
usd = SerieTaux("USD", taux_usd)

print("Devise      :", usd.devise)          # on lit un attribut
print("Moyenne     :", usd.moyenne())       # on appelle une methode
print("Variation   :", round(usd.variation(), 2), "%")
print("Minimum     :", usd.minimum())
print("Maximum     :", usd.maximum())


# =====================================================================
# B.2 : PLUSIEURS OBJETS + attribut de classe vs attribut d'instance
# =====================================================================

# --- On cree un DEUXIEME objet, pour la livre (GBP) ---
taux_gbp = charger_taux("donnees/taux_EUR_GBP.csv")
gbp = SerieTaux("GBP", taux_gbp)

# Chaque objet a SES PROPRES donnees (attributs d'instance)
print("\n--- Deux objets, chacun ses donnees ---")
print("USD moyenne :", round(usd.moyenne(), 4))
print("GBP moyenne :", round(gbp.moyenne(), 4))


# --- Attribut de CLASSE : partage par tous les objets ---
class SerieTaux2:
    base = "EUR"    # attribut de CLASSE : le meme pour tous les objets

    def __init__(self, devise, taux):
        self.devise = devise   # attribut d'INSTANCE : propre a chaque objet
        self.taux = taux

s1 = SerieTaux2("USD", [1.17, 1.16])
s2 = SerieTaux2("GBP", [0.85, 0.86])

print("\n--- Attribut de classe (partage) ---")
print("Base de s1 :", s1.base)    # EUR
print("Base de s2 :", s2.base)    # EUR (le meme, partage)
print("Devise de s1 :", s1.devise)  # USD (propre a s1)
print("Devise de s2 :", s2.devise)  # GBP (propre a s2)


# =====================================================================
# B.3 : LES DATACLASSES (ecriture raccourcie)
# =====================================================================
from dataclasses import dataclass

# Le decorateur @dataclass ecrit __init__ automatiquement pour nous
@dataclass
class SerieTauxSimple:
    devise: str        # attribut de type texte
    taux: list         # attribut de type liste

    # On peut quand meme ajouter des methodes
    def moyenne(self):
        return sum(self.taux) / len(self.taux)

# On cree un objet exactement comme avant
demo = SerieTauxSimple("USD", [1.17, 1.16, 1.19])

print("\n--- Dataclass ---")
print("Devise  :", demo.devise)
print("Taux    :", demo.taux)
print("Moyenne :", round(demo.moyenne(), 4))

# Bonus : une dataclass affiche joliment son contenu automatiquement
print("Affichage auto :", demo)

