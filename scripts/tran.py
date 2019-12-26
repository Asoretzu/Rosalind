from services import fasta


def _trans_finder(b1, b2):
    transition = [["A", "G"], ["C", "T"]]

    for trans in transition:
        if b1 in trans and b2 in trans:
            return [1, 0]
    return[0, 1]


def tran(file_name):
    """
    Prints

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Transitions and Transversions

    For DNA strings s1 and s2 having the same length, their transition /
    transversion ratio R(s1,s2) is the ratio of the total number of transitions
    to the total number of transversions, where symbol substitutions are
    inferred from mismatched corresponding symbols as when calculating Hamming
    distance (see “Counting Point Mutations”).

    Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

    Return: The transition/transversion ratio R(s1,s2).

    Sample Dataset

    >Rosalind_0209
    GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
    AGTACGGGCATCAACCCAGTT
    >Rosalind_2200
    TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
    GGTACGAGTGTTCCTTTGGGT

    Sample Output
    1.21428571429
    """

    data = fasta.get(file_name)
    str1 = data[1][0]
    str2 = data[1][1]

    transitions = 0
    transversions = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            trans = _trans_finder(str1[i], str2[i])
            transitions = transitions + trans[0]
            transversions = transversions + trans[1]

    print(round(transitions/transversions, 11))
