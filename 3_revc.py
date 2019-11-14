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


def REVC():
    dna = "AAAACCCGGT"
    rdna = dna[:: -1]
    cdna = ""

    for nt in rdna:
        if nt == "A":
            cdna = cdna + "T"
        elif nt == "C":
            cdna = cdna + "G"
        elif nt == "T":
            cdna = cdna + "A"
        elif nt == "G":
            cdna = cdna + "C"

    print(cdna)

if __name__ == "__main__":
    REVC()
