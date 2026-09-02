print("PROJET PYTHON - SEANCE 1")
print()


print("A.2 - PREMIER PROGRAMME")
print("Hello, world ! Ceci est notre premier programme Python.")
print()


print("A.3 - LES TYPES DE BASE")

entier = 42
decimal = 3.14
chaine = "Bonjour"
booleen = True
liste = [1, 2, 3, "quatre"]
dictionnaire = {"nom": "Alice", "age": 30}

print(entier, type(entier))
print(decimal, type(decimal))
print(chaine, type(chaine))
print(booleen, type(booleen))
print(liste, type(liste))
print(dictionnaire, type(dictionnaire))

x = 5
print("x est un nombre :", x, type(x))
x = "du texte maintenant"
print("x est du texte :", x, type(x))

print("3" + str(4))
print(int("3") + 4)
print()


print("A.4 - LES OPERATIONS")

a = 17
b = 5
print("addition        :", a + b)
print("soustraction    :", a - b)
print("multiplication  :", a * b)
print("division        :", a / b)
print("division entiere:", a // b)
print("modulo (reste)  :", a % b)
print("puissance       :", a ** b)

print("majuscules :", "bonjour".upper())
print("decouper   :", "un deux trois".split())
print("longueur   :", len("bonjour"))

nombres = [10, 20, 30]
nombres.append(40)
print("la liste   :", nombres)
print("sa longueur:", len(nombres))
print("1er element:", nombres[0])

personne = {"nom": "Alice", "age": 30}
print("le nom     :", personne["nom"])
personne["ville"] = "Paris"
print("le dico    :", personne)

print("3 == 3 :", 3 == 3)
print("3 != 4 :", 3 != 4)
print("3 < 4  :", 3 < 4)

print("and :", True and False)
print("or  :", True or False)
print("not :", not True)
print()


print("A.5 - LES CONDITIONS")

taux = 1.08

if taux > 1:
    print("au-dessus de 1")
elif taux == 1:
    print("egal a 1")
else:
    print("en-dessous de 1")
print()


print("A.6 - LES BOUCLES")

taux_liste = [1.08, 1.09, 1.10, 1.07]

print("Avec for :")
for t in taux_liste:
    print("taux :", t)

somme = 0
for t in taux_liste:
    somme = somme + t
print("Somme :", round(somme, 4))

print("Avec while :")
i = 0
while i < len(taux_liste):
    print("taux :", taux_liste[i])
    i = i + 1
print()


print("C.1 - EXPLORER UN DICTIONNAIRE")

import copy

reponse = {
    "amount": 1.0,
    "base": "EUR",
    "date": "2024-01-02",
    "rates": {"USD": 1.0956},
}

print("date     :", reponse["date"])
print("taux USD :", reponse["rates"]["USD"])

reponse["date"] = "2099-01-01"
print("apres changement :", reponse)

copie = reponse.copy()
copie["rates"]["USD"] = 9.9999
print("original modifie aussi :", reponse["rates"])

original = {"base": "EUR", "rates": {"USD": 1.0956}}
copie_profonde = copy.deepcopy(original)
copie_profonde["rates"]["USD"] = 0.0001
print("original protege :", original["rates"])
print()


print("C.2 - APPEL DE L'API")

import json
import csv
import urllib.request
from pathlib import Path

BASE = "EUR"
DEVISE = "USD"

Path("cache").mkdir(exist_ok=True)
Path("donnees").mkdir(exist_ok=True)

try:
    url_jour = "https://api.frankfurter.app/latest?from=" + BASE + "&to=" + DEVISE
    reponse_web = urllib.request.urlopen(url_jour)
    texte = reponse_web.read().decode("utf-8")
    data_jour = json.loads(texte)

    print("Date :", data_jour["date"])
    print("Taux :", data_jour["rates"][DEVISE])

    fichier = open("cache/latest_" + BASE + "_" + DEVISE + ".json", "w")
    json.dump(data_jour, fichier, indent=2)
    fichier.close()

    url_serie = "https://api.frankfurter.app/2026-01-01..2026-09-01?from=" + BASE + "&to=" + DEVISE
    reponse_web = urllib.request.urlopen(url_serie)
    texte = reponse_web.read().decode("utf-8")
    data_serie = json.loads(texte)

    fichier = open("cache/serie_" + BASE + "_" + DEVISE + ".json", "w")
    json.dump(data_serie, fichier, indent=2)
    fichier.close()

    rates = data_serie["rates"]
    fichier_csv = open("donnees/taux_" + BASE + "_" + DEVISE + ".csv", "w", newline="")
    writer = csv.writer(fichier_csv)
    writer.writerow(["date", "devise", "taux"])
    for date in sorted(rates):
        writer.writerow([date, DEVISE, rates[date][DEVISE]])
    fichier_csv.close()

    print("Fichiers cache/ et donnees/ crees avec succes !")

except Exception as erreur:
    print("Impossible de joindre l'API (verifie ta connexion internet).")
    print("Detail :", erreur)

print()
print("FIN DU PROGRAMME")