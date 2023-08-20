from services import fasta
from services.search import amino_mass


def work(file_name):
    """Calculating Protein Mass"""

    data = fasta.get(file_name)
    mass = 0
    for amino in data:
        mass = mass + amino_mass(amino)

    print(round(mass, 3))
