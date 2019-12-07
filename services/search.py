# Get the number of possible codons tha can translate a given aminoacid
def possible_codons(amino):
    with open("data/possible_codons.txt", mode="r") as f:
        for line in f:
            prot = line[0: -1]
            prot = prot.split()

            if amino == prot[0]:
                return int(prot[1])


def amino_mass(amino):
    with open("data/aminoacid_mass.txt", mode="r") as f:
        for line in f:
            prot = line[0: -1]
            prot = prot.split()

            if amino == prot[0]:
                return float(prot[1])


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
