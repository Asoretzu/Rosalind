from services import fasta


def lcsm(file_name):
    """
    Prints the longest common substring of a collection.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Finding a Shared Motif

    A common substring of a collection of strings is a substring of every
    member of the collection. We say that a common substring is a longest
    common substring if there does not exist a longer common substring. For
    example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it
    is not as long as possible in this case, "CGTA" is a longest common
    substring of "ACGTACGT" and "AACCGTATA".

    Note that the longest common substring is not necessarily unique for a
    simple example, "AA" and "CC" are both longest common substrings of "AACC"
    and "CCAA".

    Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each
    in FASTA format.

    Return: A longest common substring of the collection. (If multiple
    solutions exist, you may return any single solution.)

    Sample Dataset

    >Rosalind_1
    GATTACA
    >Rosalind_2
    TAGACCA
    >Rosalind_3
    ATACA

    Sample Output
    AC
    """

    dataset = fasta.get(file_name)
    dataset = sorted(dataset[1], key=len)
    seq = dataset[1:]
    srtd_seq = sorted(seq, key=len)

    short_seq = srtd_seq[0]
    comp_seq = srtd_seq[1:]
    motif = ""

    for i in range(len(short_seq)):
        for j in range(i, len(short_seq)):
            m = short_seq[i: j+1]
            shared_motif = False

            for seq in comp_seq:
                if m in seq:
                    shared_motif = True
                else:
                    break

            if shared_motif and len(m) > len(motif):
                motif = m

    print(motif)
