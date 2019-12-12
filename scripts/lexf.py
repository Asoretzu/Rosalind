from services import fasta
from itertools import product


def lexf(file_name):
    """
    Prints all strings of length n that can be formed from a given string.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Enumerating k-mers Lexicographically

    Assume that an alphabet A has a predetermined order; that is, we write the
    alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance,
    the English alphabet is organized as (A,B,…,Z).

    Given two strings s and t having the same length n, we say that s precedes
    t in the lexicographic order (and write s<Lext) if the first symbol s[j]
    that doesn't match t[j] satisfies sj<tj in A.

    Given: A collection of at most 10 symbols defining an ordered alphabet, and
    a positive integer n (n≤10).

    Return: All strings of length n that can be formed from the alphabet,
    ordered lexicographically (use the standard order of symbols in the English
    alphabet).

    Sample Dataset
    A C G T
    2

    Sample Output
    AA
    AC
    AG
    AT
    CA
    CC
    CG
    CT
    GA
    GC
    GG
    GT
    TA
    TC
    TG
    TT
    """

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split("\n")

    letters = data[0]
    letters = letters.split()
    letters.sort()
    number = int(data[1])

    prod = product(letters, repeat=number)

    for p in prod:
        print("".join(map(str, p)))
