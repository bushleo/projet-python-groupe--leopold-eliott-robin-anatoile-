import argparse
import csv


# --- Petite fonction pour charger les taux d'un CSV ---
def charger(chemin):
    dates = []
    taux = []
    with open(chemin, newline="") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            dates.append(ligne[0])
            taux.append(float(ligne[2]))
    return dates, taux


# --- Les actions possibles (une fonction par sous-commande) ---
def action_analyser():
    dates, taux = charger("donnees/taux_EUR_USD.csv")
    moyenne = sum(taux) / len(taux)
    print("Analyse du taux EUR/USD :")
    print(f"  Moyenne : {moyenne:.4f}")
    print(f"  Minimum : {min(taux)}")
    print(f"  Maximum : {max(taux)}")


def action_graphiques():
    print("Generation des graphiques... (a completer)")


# =====================================================================
# D.1 : LA LIGNE DE COMMANDE avec argparse
# =====================================================================
def main():
    # On cree l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Outil du projet taux de change")

    # On ajoute des sous-commandes (analyser, graphiques)
    sous = parser.add_subparsers(dest="commande")
    sous.add_parser("analyser", help="Analyser les taux (moyenne, min, max)")
    sous.add_parser("graphiques", help="Generer les graphiques")

    # On lit ce que l'utilisateur a tape
    args = parser.parse_args()

    # On lance la bonne action selon la sous-commande
    if args.commande == "analyser":
        action_analyser()
    elif args.commande == "graphiques":
        action_graphiques()
    else:
        parser.print_help()   # si aucune commande, on affiche l'aide


# Ceci ne s'execute QUE si on lance ce fichier directement
if __name__ == "__main__":
    main()