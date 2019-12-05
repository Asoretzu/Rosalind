# ID = "SIGN"
# PROJECT = "Enumerating Oriented Gene Orderings"

# A signed permutation of length n is some ordering of the positive integers
# {1, 2, …, n} in which each integer is then provided with either a positive or
# negative sign(for the sake of simplicity, we omit the positive sign). For
# example, π= (5, −3, −2, 1, 4) is a signed permutation of length 5.

# Given: A positive integer n≤6.

# Return: The total number of signed permutations of length n, followed by a
# list of all such permutations(you may list the signed permutations in any
# order).

# Sample Dataset
# 2

# Sample Output
# 8
# -1 -2
# -1  2
#  1 -2
#  1  2
# -2 -1
# -2  1
#  2 -1
#  2  1


from services import fasta
from itertools import permutations


def sign(file_name):
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
