"""Séance 2 - Partie B : appel API protégé et journalisé."""

import json
import logging
import urllib.error
import urllib.request

logging.basicConfig(
    filename="logs/projet.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

URL = "https://api.frankfurter.app/latest?from=EUR&to=USD"


def recuperer_taux(url):
    """Appelle l'API et renvoie le dictionnaire, ou None en cas d'erreur."""
    logging.info("Appel de l'API : %s", url)
    requete = urllib.request.Request(url, headers={"User-Agent": "projet-python-bfa1"})
    try:
        with urllib.request.urlopen(requete, timeout=10) as reponse:
            texte = reponse.read().decode("utf-8")
            donnees = json.loads(texte)
    except urllib.error.HTTPError as e:
        logging.error("Erreur HTTP %s", e.code)
        print("Le serveur a refusé la demande (erreur", e.code, ")")
        return None
    except urllib.error.URLError:
        logging.error("Pas de connexion réseau")
        print("Impossible de joindre l'API : vérifiez votre connexion.")
        return None
    except json.JSONDecodeError:
        logging.error("Réponse illisible")
        print("La réponse de l'API n'est pas lisible.")
        return None
    else:
        logging.info("Réponse reçue pour la date %s", donnees["date"])
        return donnees
    finally:
        logging.info("Fin de la tentative d'appel.")


donnees = recuperer_taux(URL)

if donnees is None:
    logging.warning("Aucune donnée récupérée.")
else:
    taux = donnees["rates"]["USD"]
print("1 EUR =", taux, "USD au", donnees["date"])