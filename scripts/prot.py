from services import fasta
from services import translate


def work(file_name):
    """Translating RNA into Protein"""

    data = fasta.get(file_name)

    protein = ""

    # Get the mRNA to translate to protein
    for i in range(0, len(data)-1, 3):
        codon = data[i] + data[i+1] + data[i+2]
        c = translate.to_protein(codon)
        if c != "stop":
            protein = protein + c

    print(protein)
