# Get all the codons that transcribe aminoacids
def _coding(codon):
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
        c = _coding(codon)
        if c != "stop":
            protein = protein + c

    return(protein)
