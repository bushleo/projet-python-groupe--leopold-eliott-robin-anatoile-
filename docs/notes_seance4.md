# Notes — Séance 4

## Partie A — Python plus idiomatique

**Question 1 : C'est quoi une compréhension de liste ? Quel avantage par rapport à une boucle for classique ?**

Une compréhension de liste est une façon courte de créer une liste en une seule ligne. Par exemple, `[t * 2 for t in taux]` crée une nouvelle liste où chaque taux est multiplié par 2. L'avantage par rapport à une boucle for classique est que c'est plus court et plus lisible : là où une boucle demande trois lignes (créer une liste vide, boucler, faire append), la compréhension tient en une seule ligne claire.

**Question 2 : À quoi servent enumerate et zip ?**

enumerate sert à parcourir une liste en obtenant l'indice et la valeur en même temps (par exemple 0 → première valeur, 1 → deuxième valeur). zip sert à associer deux listes élément par élément (par exemple la première date avec le premier taux, la deuxième date avec le deuxième taux, etc.).

**Question 3 : Comment trier une liste selon un critère (sorted avec key) ?**

On utilise `sorted(liste, key=...)`. Le paramètre key indique selon quel critère trier. Par exemple, pour trier des couples (date, taux) selon le taux, on écrit `sorted(paires, key=lambda couple: couple[1])` : le `couple[1]` dit « trie d'après le deuxième élément de chaque couple », c'est-à-dire le taux.

**Question 4 : C'est quoi une f-string ? Comment afficher un nombre à deux décimales ?**

Une f-string est une chaîne de caractères qui commence par `f"..."` et dans laquelle on peut insérer des variables entre accolades. Pour afficher un nombre à deux décimales, on écrit `f"{taux:.2f}"` : le `:.2f` signifie « affiche ce nombre avec deux chiffres après la virgule ».

**Question 5 : C'est quoi une fonction lambda ?**

Une fonction lambda est une mini-fonction écrite en une seule ligne, sans nom. Par exemple, `lambda t: t * 100` est une fonction qui prend t et renvoie t multiplié par 100. On l'utilise souvent avec map (appliquer à toute une liste), filter (garder certains éléments), ou comme critère dans sorted.



## Partie B — La programmation orientée objet (les classes)

**Question 1 : C'est quoi une classe ? Un objet ? Une instance ? À quoi sert self ?**

Une classe est un modèle qui regroupe des données et des fonctions. Un objet (aussi appelé instance) est un exemplaire concret créé à partir de cette classe, avec ses propres données. Par exemple, SerieTaux est la classe (le modèle) et usd est un objet (un exemplaire rempli avec les taux du dollar).

self désigne l'objet lui-même. Dans les méthodes, self permet d'accéder aux données de l'objet sur lequel on travaille : quand on écrit `self.taux`, on parle des taux de cet objet précis. C'est ce qui permet à chaque objet de travailler sur ses propres données.

**Question 2 : À quoi sert __init__ ?**

`__init__` est une méthode spéciale, appelée automatiquement au moment où l'on crée un objet. Elle sert à remplir l'objet avec ses données de départ. Par exemple, `self.devise = devise` range la devise dans l'objet dès sa création.

**Question 3 : Différence entre un attribut de classe et un attribut d'instance ?**

Un attribut d'instance est propre à chaque objet : il est défini dans `__init__` avec `self.` (par exemple la devise et les taux, différents pour chaque objet). Un attribut de classe est partagé par tous les objets : il est défini directement dans la classe, sans self (par exemple la devise de base EUR, commune à toutes les séries).

Attention au piège : si un attribut de classe est une liste ou un dictionnaire (mutable), il est partagé par tous les objets ; si un objet le modifie, tous les autres voient la modification. Les données modifiables doivent donc être des attributs d'instance.

**Question 4 : Qu'apporte une dataclass par rapport à une classe écrite entièrement à la main ?**

Une dataclass écrit automatiquement la méthode `__init__` : on déclare seulement les attributs, sans avoir à écrire les `self.x = x` à la main. Elle fournit aussi un affichage automatique et lisible de l'objet avec print. Cela évite du code répétitif, ce qui est pratique quand une classe sert surtout à regrouper des données.


## Partie C — Visualiser avec matplotlib

**Question 1 : Différence entre la figure et les axes ? Pourquoi préférer fig, ax = plt.subplots() à l'usage direct de pyplot ?**

La figure est l'image entière (la feuille de dessin). Les axes sont la zone de dessin à l'intérieur, où la courbe est réellement tracée (avec l'axe horizontal x et l'axe vertical y). Une figure peut contenir plusieurs axes (plusieurs graphiques côte à côte).

On préfère `fig, ax = plt.subplots()` parce que c'est plus clair et plus contrôlable : on manipule explicitement la figure et les axes, donc on sait exactement sur quel graphique on dessine. C'est indispensable dès qu'on a plusieurs graphiques dans une même image. L'usage direct de pyplot (`plt.plot(...)`) est plus simple pour un seul graphique rapide, mais devient confus dès qu'on a plusieurs zones de dessin.

**Question 2 : Quel type de graphique pour quel type de donnée (série temporelle, distribution, comparaison) ?**

- Pour une série temporelle (une évolution dans le temps, comme un taux jour après jour) : une courbe (`plot`).
- Pour une distribution (comment se répartissent des valeurs, comme les variations quotidiennes) : un histogramme (`hist`).
- Pour une comparaison (plusieurs devises) : plusieurs courbes sur un même graphique avec une légende, ou plusieurs graphiques côte à côte (subplots).

**Question 3 : Comment sauvegarder une figure en PNG ?**

On utilise `plt.savefig("nom_du_fichier.png")`. Cela enregistre le graphique sous forme d'image PNG dans le dossier du projet. On appelle souvent `plt.tight_layout()` juste avant pour bien ajuster la mise en page et éviter que les titres ou les étiquettes soient coupés.


## Partie D — Assembler et finaliser

**Question 1 : À quoi sert argparse ? Pourquoi une ligne de commande plutôt que des input() ?**

argparse sert à créer un outil en ligne de commande : il lit les mots et options que l'utilisateur tape après le nom du fichier (par exemple `outil.py analyser`) et lance la bonne action.

On préfère une ligne de commande à des input() parce que c'est plus rapide et pratique : on donne toutes les instructions d'un coup dans la commande, au lieu que le programme s'arrête pour poser des questions une par une. C'est aussi automatisable (on peut mettre la commande dans un script) et c'est la façon standard dont fonctionnent les vrais outils (comme git).

**Question 2 : Que fait exactement if __name__ == "__main__" ?**

Cette ligne fait en sorte que le code qu'elle contient ne s'exécute que si le fichier est lancé directement (avec `python3 outil.py`). Si le fichier est importé depuis un autre fichier, ce code ne se déclenche pas.

C'est utile pour séparer le code « à exécuter quand on lance le programme » et les fonctions « juste définies pour être réutilisées ailleurs ». Sans cette ligne, importer le fichier lancerait tout le programme, ce qu'on ne veut pas.

**Question 3 : C'est quoi un module ? Un package ?**

Un module est un fichier Python (un fichier `.py`) qui contient du code (fonctions, classes) réutilisable ailleurs avec import. Par exemple, `outil.py` est un module.

Un package est un dossier qui regroupe plusieurs modules pour organiser un projet plus gros. C'est comme un classeur qui range plusieurs feuilles.

**Question 4 : Que doit contenir un bon README ? À quoi servent requirements.txt et .gitignore ?**

Un bon README doit contenir : une description du projet, les noms du groupe, les instructions d'installation et des exemples de commandes pour l'utiliser. Il permet à quelqu'un qui découvre le projet de comprendre à quoi il sert et comment le faire fonctionner.

Le requirements.txt liste les librairies nécessaires au projet (pandas, numpy...), pour que quelqu'un puisse toutes les installer d'un coup avec `pip install -r requirements.txt`.

Le .gitignore liste les fichiers et dossiers que Git doit ignorer (ne pas envoyer sur GitHub), comme les fichiers temporaires ou les dossiers d'environnement. Cela garde le dépôt propre.