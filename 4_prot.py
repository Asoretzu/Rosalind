# ID = "PROT"
# PROJECT = "Translating RNA into Protein"

# The 20 commonly occurring amino acids are abbreviated by using 20 letters from
# the English alphabet (all letters except for B, J, O, U, X, and Z). Protein
# strings are constructed from these 20 symbols. Henceforth, the term genetic
# string will incorporate protein strings along with DNA strings and RNA strings.

# The RNA codon table dictates the details regarding the encoding of specific
# codons into the amino acid alphabet.

# Given: An RNA string "s" corresponding to a strand of mRNA (of length at most
# 10 kbp).

# Return: The protein string encoded by s.

# The RNA codon table
# UUU F      CUU L      AUU I      GUU V
# UUC F      CUC L      AUC I      GUC V
# UUA L      CUA L      AUA I      GUA V
# UUG L      CUG L      AUG M      GUG V
# UCU S      CCU P      ACU T      GCU A
# UCC S      CCC P      ACC T      GCC A
# UCA S      CCA P      ACA T      GCA A
# UCG S      CCG P      ACG T      GCG A
# UAU Y      CAU H      AAU N      GAU D
# UAC Y      CAC H      AAC N      GAC D
# UAA Stop   CAA Q      AAA K      GAA E
# UAG Stop   CAG Q      AAG K      GAG E
# UGU C      CGU R      AGU S      GGU G
# UGC C      CGC R      AGC S      GGC G
# UGA Stop   CGA R      AGA R      GGA G
# UGG W      CGG R      AGG R      GGG G

# Sample Dataset
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

# Sample Output
# MAMAPRTEINSTRING


def coding(codon):

    # All codons that transcribe aminoacids
    if codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
        return "A"

    if codon == "UGU" or codon == "UGC":
        return "C"

    if codon == "GAU" or codon == "GAC":
        return "D"

    if codon == "GAA"  or codon == "GAG":
        return "E"

    if codon == "UUU" or codon == "UUC":
        return "F"

    if codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG":
        return "G"

    if codon == "CAU" or codon == "CAC":
        return "H"

    if codon == "AUU" or codon == "AUC" or codon == "AUA":
        return "I"

    if codon == "AAA" or codon == "AAG":
        return "K"

    if codon == "CUU" or codon == "CUC" or codon == "UUA" or codon == "CUA" or codon == "UUG" or codon == "CUG":
        return "L"

    if codon == "AUG":
        return "M"

    if codon == "AAU" or codon == "AAC":
        return "N"

    if codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
        return "P"

    if codon == "CAA" or codon == "CAG":
        return "Q"

    if codon == "CGU" or codon == "CGC" or codon == "CGA" or codon == "AGA" or codon == "CGG" or codon == "AGG":
        return "R"

    if codon == "UCU" or codon == "UCA" or codon == "UCC" or codon == "UCG" or codon == "AGU" or codon == "AGC":
        return "S"

    if codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
        return "T"

    if codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
        return "V"

    if codon == "UGG":
        return "W"

    if codon == "UAU" or codon == "UAC":
        return "Y"

    if codon == "UAG" or codon == "UAA" or codon == "UGA":
        return "stop"


def PROT():
    dataset = ""
    # dataset = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    protein = ""

    with open("TXT/rosalind_prot.txt", mode="r") as f:
        for line in f:
            dataset = dataset + line

    # Get the mRNA to translate to protein
    for i in range(0, len(dataset)-1, 3):
        codon = dataset[i] + dataset[i+1] + dataset[i+2]
        c = coding(codon)
        if c != "stop":
            protein = protein + c

    print(protein)


if __name__ == "__main__":
    PROT()
