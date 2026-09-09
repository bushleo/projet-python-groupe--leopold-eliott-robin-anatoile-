"""Séance 2 - Partie C : récursivité, mémoïsation et complexité."""

import time
from functools import lru_cache


def factorielle(n):
    """Calcule n! de façon récursive."""
    if n <= 1:
        return 1
    return n * factorielle(n - 1)


def fib_naif(n):
    """Fibonacci récursif naïf."""
    if n < 2:
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)


@lru_cache(maxsize=None)
def fib_memo(n):
    """Fibonacci récursif avec mémoïsation."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_iteratif(n):
    """Fibonacci avec une boucle."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def chronometrer(fonction, n):
    """Mesure le temps d'exécution en secondes."""
    debut = time.perf_counter()
    fonction(n)
    return time.perf_counter() - debut


print("factorielle(10) =", factorielle(10))
print()
print("n    | naif        | memo        | iteratif")

for n in [10, 20, 25, 30, 32, 35]:
    t1 = chronometrer(fib_naif, n)
    fib_memo.cache_clear()
    t2 = chronometrer(fib_memo, n)
    t3 = chronometrer(fib_iteratif, n)
    print(n, " |", round(t1, 6), "|", round(t2, 6), "|", round(t3, 6))