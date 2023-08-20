from services import fasta


def work(file_name):
    """Complementing a Strand of DNA."""

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

    print(complement_dna)
