from itertools import permutations
from services import fasta


def perm(file_name):
    """Enumerating Gene Orders"""

    n = int(fasta.get(file_name))
    lista = []

    for i in range(1, n+1):
        lista.append(i)

    perm = permutations(lista)

    total = 1
    for i in range(1, n+1):
        total = total * i

    print(total)

    for i in list(perm):
        print(" ".join(map(str, i)))
