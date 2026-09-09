Partie A

A.1/A.2 — Question 1 : C'est quoi Python ? À quoi ça sert ? Compilé ou interprété ?

Python est un langage de programmation créé en 1991. Il est apprécié parce qu'il est facile à lire et à écrire. On l'utilise pour plein de choses : créer des sites web, faire de l'analyse de données et de l'intelligence artificielle, automatiser des tâches répétitives, ou faire des petits scripts.

Python est un langage interprété : on n'a pas besoin de le transformer en programme avant de le lancer, un logiciel appelé « interpréteur » lit le code et l'exécute directement. (En vrai il fait une petite étape intermédiaire en coulisses, mais pour nous on le considère comme interprété.)

A.1/A.2 — Question 2 : Comment on installe Python et comment on vérifie ?

On installe Python en le téléchargeant sur le site officiel python.org, ou avec un outil d'installation selon l'ordinateur (Homebrew sur Mac, apt sur Linux, le Microsoft Store sur Windows). Sur Windows, il faut penser à cocher la case « Add Python to PATH ».

Pour vérifier que ça a marché, on ouvre un terminal et on tape :

python --version

Ça affiche le numéro de version (par exemple Python 3.12.4). Si un numéro s'affiche, c'est que Python est bien installé, et on voit du coup quelle version on a.

A.1/A.2 — Question 3 : Les différentes façons de lancer du code Python.

Le mode interactif : on tape python dans le terminal et on écrit ligne par ligne. Utile pour tester vite fait un petit truc.
Lancer un fichier .py : on tape python monfichier.py. Utile pour faire tourner un vrai programme complet.
Un notebook Jupyter : des cases de code dans le navigateur. Utile pour l'analyse de données, quand on veut voir le code et les résultats ensemble.
Un éditeur (VS Code, PyCharm) : on clique sur un bouton « Exécuter ». Utile pour travailler sur un vrai projet avec plusieurs fichiers.

A.3 — Question 1 : Les types de base, le typage dynamique, et "3" + 4 ?

Les types de base en Python sont : les entiers (int), les nombres à virgule (float), le texte (str), les vrai/faux (bool), les listes (list) et les dictionnaires (dict).

Le typage dynamique veut dire qu'on n'a pas besoin de dire à l'avance quel type contient une variable : Python le devine tout seul selon ce qu'on met dedans. Et une variable peut même changer de type en cours de route (on peut mettre un nombre, puis du texte).

"3" + 4 provoque une erreur. Le problème c'est que "3" est du texte (à cause des guillemets) et 4 est un nombre. Python ne sait pas s'il doit coller les deux comme du texte ou les additionner comme des nombres, donc il refuse. Pour que ça marche, il faut choisir : soit "3" + str(4) qui donne "34" (on colle deux textes), soit int("3") + 4 qui donne 7 (on additionne deux nombres).

A.4 — Question 1 : Différence entre opérateur booléen et opérateur logique ?

Les opérateurs booléens and, or, not servent à combiner des conditions (des vrai/faux). Par exemple « si tu as plus de 18 ans et que tu as ta carte ».
Les opérateurs logiques bit à bit &, |, ^ travaillent sur les nombres au niveau binaire (les 0 et les 1 qui composent un nombre).

En résumé : and/or/not répondent à « c'est vrai ou faux ? », alors que &/|/^ bricolent directement les nombres en binaire.

A.6 — Question 1 : Quand utiliser une boucle for et quand une boucle while ?

On utilise for quand on sait déjà sur quoi on veut boucler : parcourir une liste, un texte, ou une plage de nombres. On connaît le nombre de tours à l'avance.
On utilise while quand on veut répéter tant qu'une condition est vraie, sans savoir combien de fois ça va durer. Par exemple : redemander un mot de passe tant qu'il est faux.
Partie B

B — Question 1 : C'est quoi Git ? C'est quoi GitHub ? La différence ?

Git est un logiciel installé sur ton ordinateur qui sauvegarde l'historique de ton code. À chaque fois que tu fais un « commit », il enregistre une version. Tu peux revenir en arrière et créer des branches.
GitHub est un site internet qui héberge ton code en ligne. Il permet de partager le projet, de travailler à plusieurs, de faire des « pull requests », etc.

La différence : Git c'est l'outil (sur ta machine), GitHub c'est le site (sur internet) qui stocke et partage le travail. On peut utiliser Git sans GitHub, et il existe d'autres sites comme GitLab.

B — Question 2 : Pourquoi utiliser Git et GitHub ?

Pour garder l'historique : on sait qui a modifié quoi et quand.
Pour revenir en arrière : si on casse quelque chose, on peut retourner à une version qui marchait.
Pour travailler à plusieurs : chacun bosse de son côté sans écraser le travail des autres.
Pour sauvegarder : le code est en ligne, donc en sécurité même si l'ordinateur plante.
Partie C

C.1 — Question 1 : Si on met une clé qui existe déjà dans un dictionnaire, il se passe quoi ? Peut-il y avoir deux fois la même clé ?

Si on donne une valeur à une clé qui existe déjà, l'ancienne valeur est remplacée par la nouvelle. Un dictionnaire ne peut pas avoir deux fois la même clé : les clés sont uniques. Réécrire une clé ne fait que changer sa valeur.

C.1 — Question 2 : Après une copie avec .copy(), si on modifie la copie, l'original change ? Et pour une partie imbriquée ?

Si on modifie une valeur « normale » (de premier niveau) dans la copie, l'original ne change pas.
Mais si on modifie une partie imbriquée (un dictionnaire à l'intérieur du dictionnaire, comme rates), alors l'original change aussi. C'est parce que .copy() fait une copie « superficielle » : les parties imbriquées sont partagées entre l'original et la copie.

C.1 — Question 3 : C'est quoi la mutabilité ? Différence entre copie superficielle et copie profonde ? Comment faire une copie profonde ?

La mutabilité, c'est le fait qu'un objet peut être modifié après sa création. Une liste ou un dictionnaire peuvent changer (mutables) ; un nombre ou du texte ne changent pas (immuables).
Une copie superficielle (.copy()) recopie le dictionnaire, mais les parties imbriquées restent partagées avec l'original.
Une copie profonde recopie vraiment tout, y compris les parties imbriquées, donc la copie est totalement indépendante.
Pour faire une copie profonde, on utilise le module copy :
import copy
ma_copie = copy.deepcopy(original)

C.1 — Question 4 : Quels types sont mutables ? Lesquels sont immuables ?

Mutables (modifiables) : les listes (list), les dictionnaires (dict), les ensembles (set).
Immuables (non modifiables) : les nombres (int, float), les vrai/faux (bool), le texte (str), les tuples (tuple).

C.2 — Question 1 : C'est quoi une API ? C'est quoi « envoyer une requête » ? C'est quoi le JSON et ça devient quoi en Python ?

Une API, c'est un service qui permet à deux programmes de se parler. Ici, on demande à l'API de la BCE les taux de change, et elle nous les envoie.
Envoyer une requête, ça veut dire faire une demande à un serveur, en gros en allant chercher une adresse internet (une URL). Le serveur nous renvoie une réponse.
Le JSON, c'est un format de texte pour ranger des données, organisé en clés et valeurs (ça ressemble beaucoup à un dictionnaire Python). Quand on le récupère en Python, il se transforme automatiquement : les accolades {} deviennent un dictionnaire, les crochets [] deviennent une liste, le texte devient une chaîne, les nombres deviennent des nombres, true/false deviennent True/False, et null devient None.

C.2 — Question 2 : Pourquoi enregistrer la réponse de l'API dans un fichier (cache/) plutôt que de rappeler l'API à chaque fois ?

C'est plus rapide : lire un fichier sur son ordinateur va plus vite que d'aller sur internet à chaque fois.
C'est plus prudent : on ne surcharge pas le serveur, et le programme marche même si internet est coupé ou si l'API est en panne.
C'est plus fiable : on garde une copie exacte des données reçues, donc on peut refaire les calculs plus tard sur les mêmes chiffres.