from services import fasta


def subs(file_name):
    """
    Prints all locations of the string t as a substring of the string s.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Finding a Motif in DNA

    Given two strings s and t, t is a substring of s if t is contained as a
    contiguous collection of symbols in s (as a result, t must be no longer
    than s).

    The position of a symbol in a string is the total number of symbols found
    to its left, including itself (e.g., the positions of all occurrences of
    'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at
    position i of s is denoted by s[i].

    A substring of s can be represented as s[j:k], where j and k represent
    the starting and ending positions of the substring in s; for example, if
    s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

    The location of a substring s[j:k] is its beginning position j; note that t
    will have multiple locations in s if it occurs more than once as a
    substring of s (see the Sample below).

    Given: Two DNA strings s and t (each of length at most 1 kbp).

    Return: All locations of t as a substring of s.

    Sample Dataset
    GATATATGCATATACTT
    ATAT

    Sample Output
    2 4 10
    """

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split()

    dataset = data[0]
    motif = data[1]

    length = len(motif)
    count = []

    # Search for motifs in the dataset
    for i in range(0, len(dataset)):
        if motif == dataset[i:i+length]:
            count.append(i+1)

    print(" ".join(str(n) for n in count))
