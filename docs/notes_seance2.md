# Notes — Séance 2

## Partie A — Les fonctions

1. 

Découper en fonctions permet de séparer le programme en petits morceaux qui font chacun une seule chose.

Trois bénéfices :

On peut réutiliser : notre fonction lire_csv peut resservir dans un autre fichier sans avoir à réécrire tout le code de lecture.
C'est plus facile à lire : quand on voit moyenne(valeurs), on comprend tout de suite ce que ça fait sans lire le détail des calculs.
C'est plus facile à corriger : si la moyenne est fausse, on sait qu'il faut regarder dans la fonction moyenne, on ne cherche pas partout.

2. 

Le paramètre, c'est ce qu'on donne à la fonction pour qu'elle travaille. La valeur de retour, c'est le résultat qu'elle nous rend.

Dans notre fonction moyenne(taux), taux est le paramètre : c'est la liste des taux qu'on lui envoie. Le return sum(taux) / len(taux) est la valeur de retour : c'est la moyenne qu'elle nous rend.

Une fonction sans return renvoie None, qui veut dire « rien ».

3. 

Une docstring est un texte entre triples guillemets """ qui explique ce que fait la fonction. On la place juste en dessous de la ligne def, avant le code.

Par exemple dans notre code :

python
def factorielle(n):
    """Calcule n! de façon récursive."""

Ça sert à ce qu'une autre personne (ou nous-mêmes plus tard) comprenne à quoi sert la fonction sans avoir à lire tout le code.

4. 

Une variable locale est créée à l'intérieur d'une fonction. Elle n'existe que pendant que la fonction tourne et disparaît après. On ne peut pas l'utiliser ailleurs dans le programme.

Une variable globale est créée en dehors des fonctions. Elle existe pendant tout le programme et on peut l'utiliser partout.

Dans notre recuperer_donnees.py, URL est globale : elle est écrite en dehors de toute fonction. Dans lire_csv, la variable couples est locale : elle n'existe que le temps que la fonction s'exécute.

## Partie B — Gérer les erreurs (try/except) et journaliser (logging)

1. 

On gère les erreurs pour que le programme ne s'arrête pas brutalement quand quelque chose se passe mal. Par exemple si internet ne marche pas, on préfère afficher un message clair plutôt que de laisser le programme planter.

Si une exception n'est pas gérée, le programme s'arrête net et affiche un long message d'erreur rouge (un « traceback »). C'est ce qui nous est arrivé la première fois avec l'erreur 403 : on avait une trentaine de lignes illisibles au lieu d'une phrase.

Le `else` s'exécute seulement si le `try` s'est bien passé, sans erreur. Le `finally` s'exécute dans tous les cas, qu'il y ait eu une erreur ou non. Dans notre code, le `finally` écrit « Fin de la tentative d'appel » dans le log à chaque fois.

2. 

Parce qu'il attrape toutes les erreurs sans distinction, et du coup on ne sait pas ce qui s'est vraiment passé. Le programme continue comme si de rien n'était et peut afficher un message faux.

On en a eu un exemple concret dans notre code de la séance 1 : on avait un `except Exception` qui affichait « Impossible de joindre l'API, vérifie ta connexion internet ». Sauf que le vrai problème n'était pas la connexion, c'était une erreur 403 (le serveur refusait notre demande). On a cru que les fichiers avaient été créés alors que non, et on ne s'en est rendu compte qu'à la séance 2.

Il vaut mieux préciser le type d'erreur, comme dans notre `appel_api.py` où on a un `except` séparé pour l'erreur HTTP, un pour le réseau et un pour le JSON illisible.

3. 

`logging` est un module de la bibliothèque standard qui sert à garder une trace de ce que fait le programme, en écrivant dans un fichier avec la date et l'heure.

On le préfère à `print` parce que :
- les messages sont enregistrés dans un fichier, donc on peut les relire plus tard même si on a fermé le terminal
- chaque ligne a la date et l'heure, ce qui permet de savoir quand le problème est arrivé
- on peut choisir le niveau de détail sans supprimer les lignes du code

Les niveaux :
- **debug** : détails techniques utiles seulement quand on cherche un bug
- **info** : le déroulement normal, par exemple « Appel de l'API »
- **warning** : quelque chose de suspect mais pas bloquant, par exemple aucune donnée récupérée
- **error** : une vraie erreur, par exemple l'erreur HTTP 403
- **critical** : une erreur grave qui empêche le programme de continuer

Dans notre `appel_api.py`, on utilise `info` au début de l'appel, `error` dans chaque `except`, et `warning` si on n'a récupéré aucune donnée.

## Partie C — Récursivité et complexité

1.

La récursivité, c'est quand une fonction s'appelle elle-même pour résoudre un problème plus petit, jusqu'à arriver à un cas simple qu'elle sait résoudre directement.

Le cas de base est la condition qui arrête la récursion. Le cas récursif est la partie où la fonction s'appelle elle-même.

Dans notre `factorielle(n)` :
- cas de base : `if n <= 1: return 1`
- cas récursif : `return n * factorielle(n - 1)`

Si le cas de base est absent, la fonction s'appelle indéfiniment et Python finit par arrêter le programme avec une `RecursionError`, parce qu'il y a une limite au nombre d'appels empilés.

2. 

On l'utilise parce que pour certains problèmes, elle donne un code très court et proche de la définition mathématique. La factorielle s'écrit en trois lignes.

Mais ce n'est pas toujours le meilleur choix. Notre contre-exemple, c'est Fibonacci en version naïve. Pour n = 35, notre version récursive met 5 secondes, alors que la version avec une boucle met 0,000007 seconde. C'est parce que la version récursive recalcule sans arrêt les mêmes valeurs : pour calculer fib(35), elle recalcule fib(30) des milliers de fois.

3. 

La complexité temporelle, c'est le nombre d'opérations que fait le programme selon la taille n de l'entrée. La complexité spatiale, c'est la mémoire supplémentaire qu'il utilise.

- O(n) : le temps augmente proportionnellement à n. Si on double n, le temps double. C'est le cas d'une simple boucle, comme notre `fib_iteratif`.
- O(n²) : deux boucles imbriquées. Si on double n, le temps est multiplié par 4.
- O(2ⁿ) : le temps double à chaque fois qu'on ajoute 1 à n. C'est notre Fibonacci naïf, et ça explique pourquoi il explose si vite.

Nos mesures le montrent bien : entre n = 10 et n = 35, la version naïve passe de 0,000034 s à 5 secondes, alors que les deux autres ne bougent presque pas.

4. 

La mémoïsation consiste à retenir les résultats déjà calculés pour ne pas les recalculer. Quand la fonction est rappelée avec la même valeur, elle rend directement le résultat gardé en mémoire.

`functools.lru_cache` fait ça automatiquement : il suffit d'écrire `@lru_cache(maxsize=None)` au-dessus de la fonction. Dans notre code, ça fait passer Fibonacci de 5 secondes à 0,000025 seconde pour n = 35. En contrepartie, ça occupe de la mémoire pour stocker les résultats.

Python limite la profondeur de récursion (environ 1000 appels par défaut) parce que chaque appel occupe de la place en mémoire. Sans cette limite, une récursion sans fin ferait planter tout l'ordinateur. Quand on dépasse, on obtient une `RecursionError`.

## Tableau des mesures — trois versions de Fibonacci

| n | naïf (s) | mémoïsé (s) | itératif (s) |
|---|---|---|---|
| 10 | 0,000034 | 0,000007 | 0,000003 |
| 20 | 0,0034 | 0,00001 | 0,000003 |
| 25 | 0,039461 | 0,000017 | 0,000005 |
| 30 | 0,445335 | 0,000023 | 0,000008 |
| 32 | 1,147801 | 0,000183 | 0,000007 |
| 35 | 5,000859 | 0,000025 | 0,000007 |
