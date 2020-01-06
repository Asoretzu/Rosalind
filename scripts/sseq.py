from services import fasta
from services import extras


def sseq(file_name):
    """
    Prints a collection of indices of a subsequence of a given string.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Finding a Spliced Motif

    A subsequence of a string is a collection of symbols contained in order
    (though not necessarily contiguously) in the string (e.g., ACG is a
    subsequence of TATGCTAAGATC). The indices of a subsequence are the
    positions in the string at which the symbols of the subsequence appear;
    thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

    As a substring can have multiple locations, a subsequence can have multiple
    collections of indices, and the same index can be reused in more than one
    appearance of the subsequence; for example, ACG is a subsequence of
    AACCGGTT in 8 different ways.

    Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA
    format.

    Return: One collection of indices of s in which the symbols of t appear as
    a subsequence of s. If multiple solutions exist, you may return any one.

    Sample Dataset
    >Rosalind_14
    ACGTACGTGACG
    >Rosalind_18
    GTA

    Sample Output
    3 8 10
    """

    data = fasta.get(file_name)
    string = data[1][0]
    subseq = data[1][1]

    finds = []
    pos = 0

    for i in range(len(subseq)):
        for j in range(len(string)):
            if subseq[i] == string[j]:
                if j > pos:
                    finds.append(j+1)
                    pos = j
                    break

    extras.fancy_print(finds)
