from services import fasta
from itertools import permutations


def sign(file_name):
    """Enumerating Oriented Gene Orderings"""

    num = int(fasta.get(file_name))
    string = []
    aux = set()
    result = []

    # Create a list of all the negative and positive elements
    for i in range(1, num+1):
        string.append(i)
        string.append(-i)

    # Make all the permutations
    perm = list(permutations(string, num))

    # Append only the permutations without repeated absolute values
    for item in perm:
        for i in range(len(item)):
            aux.add(abs(item[i]))
        if len(aux) == len(item):
            result.append(item)
        aux = set()

    # Print the length and every permutation
    length = len(result)
    print(length)

    for i in result:
        print(" ".join(map(str, i)))
