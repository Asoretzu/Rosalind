# ID = "ORF"
# PROJECT = "Open Reading Frames"

# Either strand of a DNA double helix can serve as the coding strand for RNA
# transcription. Hence, a given DNA string implies six total reading frames, or
# ways in which the same region of DNA can be translated into amino acids:
# three reading frames result from reading the string itself, whereas three
# more result from reading its reverse complement.

# An open reading frame (ORF) is one which starts from the start codon and ends
# by stop codon, without any other stop codons in between. Thus, a candidate
# protein string is derived by translating an open reading frame into amino
# acids until a stop codon is reached.

# Given: A DNA string s of length at most 1 kbp in FASTA format.

# Return: Every distinct candidate protein string that can be translated from
# ORFs of s. Strings can be returned in any order.


# Sample Dataset

# >Rosalind_99
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

# Sample Output

# MLLGSFRLIPKETLIQVAGSSPCNLS
# M
# MGMTPRLGLESLLE
#   MTPRLGLESLLE


# start codon: AUG
# stop codon: UAG UGA UAA


# file_name = "TXT/lalo.txt"
file_name = "TXT/rosalind_orf.txt"


def rna_trans(dna):
    rna = ""

    for nt in dna:
        if nt == "T":
            rna = rna + "U"
        else:
            rna = rna + nt

    return(rna)


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


def coding(codon):
    # All codons that transcribe aminoacids
    with open("data/rna_codons.txt", mode="r") as f:
        for line in f:
            if line != "\n":
                prot = line[0:-1]
                prot = prot.split()

                if prot[1] == "Stop":
                    return ""
                if prot[0] == codon:
                    return prot[1]


def ORF(rna):
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
                c = coding(codon)

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


if __name__ == "__main__":
    dna = ""

    with open(file_name, mode="r") as f:
        for line in f:
            if line[0] != ">":
                dna = dna + line[0:-1]

    rna = rna_trans(dna)
    ORF(rna)
