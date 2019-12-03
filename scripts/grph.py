# ID = "GRPH"
# PROJECT = "Overlap Graphs"

# A graph whose nodes have all been labeled can be represented by an adjacency
# list, in which each row of the list contains the two node labels corresponding
# to a unique edge.

# A directed graph (or digraph) is a graph containing directed edges, each of
# which has an orientation. That is, a directed edge is represented by an arrow
# instead of a line segment; the starting and ending nodes of an edge form its
# tail and head, respectively. The directed edge with tail v and head w is
# represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of
# the form (v,v).

# For a collection of strings and a positive integer k, the overlap graph for
# the strings is a directed graph Ok in which each string is represented by a
# node, and string s is connected to string t with a directed edge when there is
# a length k suffix of s that matches a length k prefix of t, as long as s≠t; we
# demand s≠t to prevent directed loops in the overlap graph (although directed
# cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length at
# most 10 kbp.

# Return: The adjacency list corresponding to O3. You may return edges in
# any order.

# Sample Dataset

# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG

# Sample Output

# Rosalind_0498 Rosalind_2391
# Rosalind_0498 Rosalind_0442
# Rosalind_2391 Rosalind_2323


# file_name = "TXT/lalo.txt"
file_name = "TXT/rosalind_grph.txt"


def GRPH(fasta_ids, fasta_codes):
    prefix = []
    suffix = []
    s = ""
    k = 3

    for set in fasta_codes:

        # Get the prefix values
        for i in range(0, k):
            s = s + set[i]
        prefix.append(s)
        s = ""

        # Get the suffix values
        for i in range (-1, (-1-k), -1):
            s = s + set[i]
        s = s[::-1]
        suffix.append(s)
        s = ""

    # Compare suffix whit prefix
    for i in range(0, len(suffix)):
        for j in range(0, len(prefix)):
            if suffix[i] == prefix[j]:
                if prefix[i] == prefix[j] and suffix[i] == suffix[j]:
                    pass
                else:
                    print("{} {}".format(fasta_ids[i], fasta_ids[j]))


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

    GRPH(fasta_ids, fasta_codes)
