from services import fasta
from data import aminoacid_mass


def work(file_name):
    """Calculating Protein Mass"""

    data = fasta.get(file_name)

    mass = 0
    for amino in data:
        mass = mass + aminoacid_mass[amino]

    print(round(mass, 3))
