from services import fasta
from services.math import fact


def pmch(file_name):
    """Perfect Matchings and RNA Secondary Structures"""

    dataset = fasta.get(file_name)

    data = dataset[1]

    AU = data.count("A")
    GC = data.count("G")

    result = fact(AU) * fact(GC)
    print(result)
