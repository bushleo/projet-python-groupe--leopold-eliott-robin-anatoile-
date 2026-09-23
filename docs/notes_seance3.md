# Notes — Séance 3

## Partie A — Découvrir pandas

**Question 1 : C'est quoi un DataFrame ? Une Series ?**

Un DataFrame est un tableau entier, avec des lignes et des colonnes, comme une feuille Excel. C'est ce qu'on obtient avec `pd.read_csv`. Une Series est une seule colonne de ce tableau : quand on écrit `df["taux"]`, on récupère une Series. Un DataFrame est donc composé de plusieurs Series (une par colonne).

**Question 2 : Pourquoi utiliser pandas plutôt que des boucles et le module csv ? Que signifie « vectorisation » ?**

Avec le module csv, il fallait écrire une boucle for pour parcourir chaque ligne et calculer par exemple une moyenne. Avec pandas, on écrit simplement `df["taux"].mean()` : c'est plus court, plus lisible et plus rapide.

La vectorisation, c'est le fait d'appliquer une opération sur toute une colonne d'un seul coup, au lieu de la faire valeur par valeur dans une boucle. Par exemple, `df["taux"] * 100` multiplie toutes les valeurs en une seule opération. En coulisses, pandas utilise du code très optimisé, donc beaucoup plus rapide qu'une boucle Python.

**Question 3 : Pourquoi déconseille-t-on iterrows() ?**

`iterrows()` permet de parcourir un DataFrame ligne par ligne, comme une boucle. Le problème est que cela annule l'intérêt de pandas : c'est lent (on revient à une boucle Python) et le code est plus long. La bonne pratique est d'utiliser des opérations vectorisées sur toute la colonne plutôt que de boucler ligne par ligne.

**Question 4 : Comment pandas représente-t-il les valeurs manquantes (NaN) ? Conséquences sur les moyennes ?**

Quand une valeur manque, pandas la remplace par NaN (« Not a Number », c'est-à-dire « pas de valeur »). C'est le trou dans le tableau.

Pour les moyennes, par défaut `.mean()` ignore les NaN et calcule la moyenne uniquement sur les valeurs présentes. Cela évite les erreurs, mais si beaucoup de valeurs manquent, la moyenne ne porte que sur une petite partie des données et peut donc être trompeuse.



## Partie B — Nettoyer, consolider et analyser

**Question 1 : C'est quoi le forward-fill ? Quelle hypothèse fait-on en l'utilisant ?**

Le forward-fill (« remplir vers l'avant ») consiste à combler un trou dans les données en recopiant la dernière valeur connue. La BCE ne publie pas de taux les week-ends et jours fériés : ces jours-là sont vides (NaN). Le forward-fill les remplit avec le taux du dernier jour ouvré précédent (par exemple, le 1er janvier reçoit le taux du 31 décembre).

L'hypothèse faite en l'utilisant est que le taux n'a pas changé pendant le jour manquant : on suppose qu'il est resté au dernier niveau connu. C'est raisonnable pour un jour férié (le marché de référence est fermé, il n'y a pas de nouvelle cotation), mais c'est une approximation : on remplit une valeur qu'on n'a pas réellement mesurée.

**Question 2 : À quoi sert resample ? Que signifie une moyenne mobile ?**

resample sert à changer le rythme des données, par exemple passer de données journalières à des données mensuelles. Au lieu d'avoir une valeur par jour, on regroupe par mois et on calcule la moyenne de chaque mois. Cela donne une vue plus synthétique et fait ressortir la tendance mois par mois.

Une moyenne mobile est une moyenne calculée sur une fenêtre glissante de plusieurs jours (ici 7 jours). Pour chaque jour, on fait la moyenne des 7 derniers jours, puis la fenêtre se décale d'un cran au jour suivant. Cela lisse la courbe : les petites variations quotidiennes sont atténuées et on voit mieux la tendance de fond.


## Partie C — Les jointures

**Question 1 : Rappelez les quatre types de jointure (inner, left, right, outer) : que garde chacune ?**

- inner : garde seulement les clés présentes dans les deux tables (l'intersection) ; les lignes sans correspondance des deux côtés sont supprimées.
- left : garde toutes les lignes de la table de gauche ; là où il n'y a pas de correspondance à droite, les colonnes de droite valent NaN.
- right : garde toutes les lignes de la table de droite ; là où il n'y a pas de correspondance à gauche, les colonnes de gauche valent NaN.
- outer : garde toutes les lignes des deux tables (l'union) ; NaN de chaque côté là où il manque une correspondance.

**Question 2 : Sur quelle colonne (clé) joint-on ? Que devient une ligne sans correspondance dans l'autre table ?**

On joint sur une colonne commune aux deux tables, appelée la clé (dans notre cas, la colonne date). pandas met sur la même ligne les données des deux tables qui ont la même valeur de clé. Une ligne sans correspondance dans l'autre table est soit supprimée (avec inner), soit conservée avec des NaN dans les colonnes de l'autre table (avec left, right ou outer, selon le type choisi).

**Question 3 : Pour réunir deux séries de taux sur la même période, quelle jointure choisir et pourquoi ?**

On choisit une jointure inner. Comme les deux devises couvrent exactement la même période et donc les mêmes dates, chaque date de l'une a sa correspondance dans l'autre : l'inner garde toutes les lignes sans créer de NaN. Le résultat est un tableau complet et propre. Un outer donnerait ici le même résultat puisque les dates coïncident, mais l'inner est le choix le plus sûr car il ne garde que les dates présentes dans les deux séries.

**Question 4 : Quelle différence entre merge et concat ? Dans quel cas utiliser l'un ou l'autre ?**

merge apparie deux tables sur une colonne clé et les colle côte à côte : cela ajoute des colonnes (des informations différentes sur les mêmes éléments). On l'utilise pour réunir par exemple le taux USD et le taux GBP par date.

concat empile les tables sans apparier de clé, soit les unes sous les autres (cela ajoute des lignes), soit côte à côte. On l'utilise pour rallonger un tableau avec d'autres données du même type, par exemple ajouter les taux d'une nouvelle période sous ceux déjà présents.

En résumé : merge pour ajouter des colonnes en appariant sur une clé, concat pour empiler des lignes du même type.


## Partie D — numpy et aperçu de polars

**Question 1 : Différence entre une liste Python et un tableau numpy (ndarray) ? C'est quoi un dtype ? Le broadcasting ?**

Une liste Python peut contenir n'importe quoi (nombres, texte, tout mélangé) et n'est pas optimisée pour les calculs. Un tableau numpy (ndarray) ne contient qu'un seul type de données et fait les calculs sur tout le tableau d'un coup, ce qui le rend beaucoup plus rapide.

Le dtype (« data type ») est le type des éléments du tableau (par exemple float64 pour des nombres à virgule). Tous les éléments d'un ndarray partagent le même dtype.

Le broadcasting est le fait d'appliquer une opération entre un tableau et un simple nombre : l'opération est diffusée sur toutes les cases du tableau d'un coup. Par exemple, `taux * 100` multiplie chaque valeur du tableau par 100, sans boucle.

**Question 2 : Pourquoi numpy est-il plus rapide que des boucles Python ?**

Parce que numpy effectue les opérations sur tout le tableau en une seule fois (vectorisation), avec du code très optimisé écrit en langage bas niveau (C) en dessous. Une boucle Python traite les valeurs une par une en repassant à chaque tour par l'interpréteur Python, qui est lent. De plus, un ndarray ne contient qu'un seul type de données rangé de façon compacte en mémoire, ce qui permet au processeur d'y accéder plus efficacement.

**Question 3 : Différences entre pandas et polars (langage d'implémentation, usage des cœurs, évaluation paresseuse) ? Quand choisir l'un ou l'autre ?**

- Langage d'implémentation : pandas est écrit en Python/C, polars est écrit en Rust (plus rapide).
- Usage des cœurs : pandas utilise en général un seul cœur du processeur, polars utilise plusieurs cœurs en parallèle.
- Évaluation paresseuse (lazy) : polars peut regarder l'ensemble des calculs demandés avant de les exécuter et les optimiser ; pandas exécute chaque opération immédiatement.

Quand choisir quoi : pandas reste le choix par défaut car il est très répandu, bien documenté et compatible avec beaucoup d'autres outils, ce qui le rend parfait pour apprendre et pour des jeux de données de taille normale. polars devient intéressant pour de très gros volumes de données ou quand la vitesse est critique.