# ID = "CONS"
# PROJECT = "Consensus and Profile"

# A matrix is a rectangular table of values divided into rows and columns.
# An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to
# indicate the value found at the intersection of row i and column j.

# Say that we have a collection of DNA strings, all having the same length n.
# Their profile matrix is a 4×n matrix P in which P1,j represents the number of
# times that 'A' occurs in the jth position of one of the strings, P2,j
# represents the number of times that C occurs in the jth position, and so on.

# A consensus string c is a string of length n formed from our collection by
# taking the most common symbol at each position; the jth symbol of c therefore
# corresponds to the symbol having the maximum value in the j-th column of the
# profile matrix. Of course, there may be more than one most common symbol,
# leading to multiple possible consensus strings.

# DNA String
#	  A T C C A G C T
#	  G G G C A A C T
#	  A T G G A T C T
#     A A G C A A C C
#	  T T G G A A C T
#	  A T G C C A T T
#	  A T G G C A C T

# Profile
# A   5 1 0 0 5 5 0 0
# C   0 0 1 4 2 0 6 1
# G   1 1 6 3 0 1 0 0
# T   1 5 0 0 0 1 1 6

# Consensus
#     A T G C A A C T

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
# in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several
# possible consensus strings exist, then you may return any one of them.)

# Sample Dataset

# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT

# Sample Output

# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6


# file_name = "TXT/lalo.txt"
file_name = "TXT/rosalind_cons.txt"


def CONS(codes):
    for line in codes:
        print(' '.join(map(str, line)))
    print("")

    a = 0
    c = 0
    g = 0
    t = 0
    total_a = ["A:",]
    total_c = ["C:",]
    total_g = ["G:",]
    total_t = ["T:",]

    for i in range(0, len(codes[0])):
        for line in codes:
            if line[i] == "A":
                a = a + 1
            elif line[i] == "C":
                c = c + 1
            elif line[i] == "G":
                g = g + 1
            elif line[i] == "T":
                t = t + 1

        total_a.append(a)
        a = 0
        total_c.append(c)
        c = 0
        total_g.append(g)
        g = 0
        total_t.append(t)
        t = 0

    consensus = ""
    a = 0
    c = 0
    g = 0
    t = 0

    for i in range(1, len(total_a)):
        value = max(total_a[i], total_c[i], total_g[i], total_t[i])

        if value == total_a[i]:
            consensus = consensus + "A"
        elif value == total_c[i]:
            consensus = consensus + "C"
        elif value == total_g[i]:
            consensus = consensus + "G"
        elif value == total_t[i]:
            consensus = consensus + "T"

    print(consensus)
    print(' '.join(map(str, total_a)))
    print(' '.join(map(str, total_c)))
    print(' '.join(map(str, total_g)))
    print(' '.join(map(str, total_t)))




if __name__ == "__main__":
    fasta_ids = []
    fasta_codes = []
    string = ""

    with open(file_name, mode="r") as f:
        for line in f:
            # Check for FASTA IDs
            if line[0] == ">":
                line = line[1: -1]
                fasta_ids.append(line)

                # Asign every FASTA CODE
                if len(fasta_ids) == 1:
                    pass
                else:
                    fasta_codes.append(string)
                    string = ""
            else:
                # Concatenate all the FASTA CODE
                string = string + line[0:-1]

        # Asign the last FASTA CODE
        fasta_codes.append(string)

    CONS(fasta_codes)
