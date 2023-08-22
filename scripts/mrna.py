from services import fasta
from data import possible_codons


def work(file_name):
    """Inferring mRNA from Protein"""

    data = fasta.get(file_name)

    a = 1

    for amino in data:
        a = a * possible_codons[amino]

    # Adds the Stop codon
    a = a * 3

    print(a % 1000000)
