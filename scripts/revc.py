# ID = "REVC"
# PROJECT = "Complementing a Strand of DNA"


# In DNA strings, symbols 'A' and 'T' are complements of each other, as are
# 'C' and 'G'.

# The reverse complement of a DNA string "s" is the string sc formed by
# reversing the symbols of "s", then taking the complement of each symbol
# (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string "s" of length at most 1000 bp.

# Return: The reverse complement "sc" of "s".

# Sample Dataset
# AAAACCCGGT

# Sample Output
# ACCGGGTTTT


from services import fasta


def revc(file_name):
    dna = fasta.get(file_name)
    rev_dna = dna[:: -1]
    com_dna = ""

    for nt in rev_dna:
        if nt == "A":
            com_dna = com_dna + "T"
        elif nt == "C":
            com_dna = com_dna + "G"
        elif nt == "T":
            com_dna = com_dna + "A"
        elif nt == "G":
            com_dna = com_dna + "C"

    print(com_dna)
