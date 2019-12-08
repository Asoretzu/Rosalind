# Get all the codons that transcribe aminoacids
def coding(codon):
    with open("data/rna_codons.txt", mode="r") as f:
        for line in f:
            if line != "\n":
                prot = line[0: -1]
                prot = prot.split()

                if prot[1] == "Stop":
                    return ""
                if prot[0] == codon:
                    return prot[1]


# Get the DNA string and translate it to mRNA
def to_rna(dna):
    rna = ""

    for nt in dna:
        if nt == "T":
            rna = rna + "U"
        else:
            rna = rna + nt

    return(rna)


# Get the mRNA and translate it to protein
def to_protein(rna):
    protein = ""

    for i in range(0, len(rna)-1, 3):
        codon = rna[i] + rna[i+1] + rna[i+2]
        c = coding(codon)
        if c != "stop":
            protein = protein + c

    return(protein)


# Get the complement string of a given base string.
def complement(r_p):
    trans = ""

    for i in range(0, len(r_p)):
        if r_p[i] == "A":
            trans = trans + "T"
        elif r_p[i] == "T":
            trans = trans + "A"
        elif r_p[i] == "G":
            trans = trans + "C"
        elif r_p[i] == "C":
            trans = trans + "G"
    return trans
