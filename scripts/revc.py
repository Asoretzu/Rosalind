"""Complementing a Strand of DNA."""


from services import fasta


def revc(file_name):
    """
    Prints the reverse complement of a given string.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Complementing a Strand of DNA

    In DNA strings, symbols 'A' and 'T' are complements of each other, as are
    'C' and 'G'.

    The reverse complement of a DNA string "s" is the string sc formed by
    reversing the symbols of "s", then taking the complement of each symbol
    (e.g., the reverse complement of "GTCA" is "TGAC").

    Given: A DNA string "s" of length at most 1000 bp.

    Return: The reverse complement "sc" of "s".

    Sample Dataset
    AAAACCCGGT

    Sample Output
    ACCGGGTTTT
    """

    dna = fasta.get(file_name)
    reverse_dna = dna[:: -1]
    complement_dna = ''

    for nt in reverse_dna:
        if nt == 'A':
            complement_dna += 'T'
        elif nt == 'C':
            complement_dna += 'G'
        elif nt == 'T':
            complement_dna += 'A'
        elif nt == 'G':
            complement_dna += 'C'

    return complement_dna
