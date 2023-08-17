from services import fasta
from math import factorial


def pmch(file_name):
    """Perfect Matchings and RNA Secondary Structures"""

    dataset = fasta.get(file_name)

    data = dataset[1]

    AU = data.count("A")
    GC = data.count("G")

    result = factorial(AU) * factorial(GC)
    print(result)
