"""Counting DNA Nucleotides."""

from services import fasta


def dna(file_name):
    dna = fasta.get(file_name)

    a = 0
    c = 0
    g = 0
    t = 0

    for nt in dna:
        if nt == 'A':
            a += 1
        elif nt == 'C':
            c += 1
        elif nt == 'G':
            g += 1
        elif nt == 'T':
            t += 1
        else:
            pass

    return f'{a} {c} {g} {t}'
