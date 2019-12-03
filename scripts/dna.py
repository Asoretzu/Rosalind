# ID = "DNA"
# PROJECT = "Counting DNA Nucleotides"

# A string is simply an ordered collection of symbols selected from some
# alphabet and formed into a word; the length of a string is the number of
# symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols
# 'A','C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string "s" of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number
# of times that the symbols 'A', 'C', 'G', and 'T' occur in "s".

# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

# Sample Output
# 20 12 17 21

def DNA():
    dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    a = 0
    c = 0
    g = 0
    t = 0

    for nt in dna:
        if nt == "A":
            a = a + 1
        elif nt == "C":
            c = c + 1
        elif nt == "G":
            g = g + 1
        elif nt == "T":
            t = t + 1
        else:
            pass

    print("{} {} {} {}".format(a, c, g, t))

if __name__ == "__main__":
    DNA()
