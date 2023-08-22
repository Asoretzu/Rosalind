from services import fasta
from services import translate

from data import rna_codons


def complement(rna):
    r_rna = ""

    for amino in rna:
        if amino == "A":
            r_rna = r_rna + "U"
        elif amino == "U":
            r_rna = r_rna + "A"
        elif amino == "G":
            r_rna = r_rna + "C"
        elif amino == "C":
            r_rna = r_rna + "G"

    r_rna = r_rna[::-1]
    return r_rna


def work(file_name):
    """Open Reading Frames"""

    dna = fasta.get(file_name)
    rna = translate.to_rna(dna[1])

    start = []
    protein = ""
    to_print = False
    r_rna = complement(rna)
    data = [rna, r_rna]
    proteins = []

    # Check both RNA and  its reverse complement
    for d in data:
        for i in range(0, len(d)-2):
            if d[i] + d[i+1] + d[i+2] == "AUG":
                start.append(i)

        # Get the amino acid of a given codon
        for i in start:
            for j in range(i, len(d)-2, 3):
                codon = d[j] + d[j+1] + d[j+2]
                # c = translate.coding(codon)
                c = rna_codons[codon]

                # If the codon is a Stop codon, then the string can be stored
                if codon == "UAG" or codon == "UGA" or codon == "UAA":
                    to_print = True
                    break
                protein = protein + c

            # If condition is true, store the protein string
            if to_print:
                proteins.append(protein)
                to_print = False
            protein = ""
            start = []

    proteins = set(proteins)

    for element in proteins:
        print(element)
