from services import fasta
from itertools import product


def lexf(file_name):
    """Enumerating k-mers Lexicographically"""

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split("\n")

    letters = data[0]
    letters = letters.split()
    letters.sort()
    number = int(data[1])

    prod = product(letters, repeat=number)

    for p in prod:
        print("".join(map(str, p)))
