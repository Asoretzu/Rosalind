from itertools import permutations
from services import fasta


def perm(file_name):
    """
    Prints the total number of permutations and a list of all permutations.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Enumerating Gene Orders

    A permutation of length n is an ordering of the positive integers
    {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

    Given: A positive integer n≤7.

    Return: The total number of permutations of length n, followed by a list
    of all such permutations (in any order).

    Sample Dataset
    3

    Sample Output
    6
    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1
    """

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
