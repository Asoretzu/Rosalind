from services import fasta


def rna(file_name):
    """Transcribing DNA into RNA."""

    dna = fasta.get(file_name)
    rna = ''

    for nt in dna:
        if nt == 'T':
            rna += 'U'
        else:
            rna += nt

    return rna
