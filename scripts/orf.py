from services import fasta
from services import translate
from services import search


def orf(file_name):
    """
    Prints every distinct candidate protein string that can be translated from
    ORFs of a given string.

    Keyword argument:
    file_name -- The path of the txt file to be parsed.


    Open Reading Frames

    Either strand of a DNA double helix can serve as the coding strand for RNA
    transcription. Hence, a given DNA string implies six total reading frames,
    or ways in which the same region of DNA can be translated into amino acids:
    three reading frames result from reading the string itself, whereas three
    more result from reading its reverse complement.

    An open reading frame (ORF) is one which starts from the start codon and
    ends by stop codon, without any other stop codons in between. Thus, a
    candidate protein string is derived by translating an open reading frame
    into amino acids until a stop codon is reached.

    Given: A DNA string s of length at most 1 kbp in FASTA format.

    Return: Every distinct candidate protein string that can be translated from
    ORFs of s. Strings can be returned in any order.


    Sample Dataset

    >Rosalind_99
    AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGA
    ATGATCCGAGTAGCATCTCAG


    Sample Output

    MLLGSFRLIPKETLIQVAGSSPCNLS
    M
    MGMTPRLGLESLLE
    MTPRLGLESLLE
    """

    dna = fasta.get(file_name)
    rna = translate.to_rna(dna[1])

    start = []
    protein = ""
    to_print = False
    r_rna = search.complement(rna)
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
                c = translate.coding(codon)

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
