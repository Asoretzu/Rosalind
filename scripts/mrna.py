from services import fasta
from services.search import possible_codons


def mrna(file_name):
    """Inferring mRNA from Protein"""

    data = fasta.get(file_name)

    a = 1

    for amino in data:
        a = a * possible_codons(amino)

    # Adds the Stop codon
    a = a * 3

    print(a % 1000000)
