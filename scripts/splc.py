from services import fasta
from services import translate


def work(file_name):
    """RNA Splicing"""

    dataset = fasta.get(file_name)
    introns = []

    # Asign DNA string
    dna = dataset[1][0]

    # Asign introns
    for i in range(1, len(dataset[1])):
        introns.append(dataset[1][i])

    # Get the exons of the DNA string
    for intron in introns:
        dna = dna.replace(intron, "")

    # Translate DNA to mRNA, and to amino acids
    rna = translate.to_rna(dna)
    protein = translate.to_protein(rna)

    print(protein)
