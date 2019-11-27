# ID = "LCSM"
# PROJECT = "Finding a Shared Motif"

# A common substring of a collection of strings is a substring of every member
# of the collection. We say that a common substring is a longest common
# substring if there does not exist a longer common substring. For example,
# "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as
# long as possible in this case, "CGTA" is a longest common substring of
# "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique for a simple
# example, "AA" and "CC" are both longest common substrings of "AACC" and
# "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in
# FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions
# exist, you may return any single solution.)

# Sample Dataset

# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA

# Sample Output
# AC


from services import fasta


def LCSM():
    # dataset = fasta.get("TXT/lalo.txt")
    dataset = fasta.get("TXT/rosalind_lcsm.txt")
    dataset = sorted(dataset[1], key=len)

    pattern = dataset[0]
    sequences = dataset[1:]

    find = 0
    found = []

    # Asign a substring
    for i in range(0, len(pattern)):
        for j in range(len(pattern), i+1, -1):

            # Search for shared motifs
            for seq in sequences:
                if pattern[i: j+1] in seq:
                    find = find + 1

            # Store the motif, if it is shared in all the sequences
            if find == len(sequences) and len(pattern[j: i+1]) < len(pattern):
                print("Found: {}.".format(pattern[i: j+1]))
                found.append(pattern[i: j+1])
            find = 0

    # Print the longest shared motif
    found = sorted(found, key=len)
    print("This is the one: {}.".format(found[-1]))
    print("")

    # CGCACGACACTAGCCCTGTTTAGATAAGCTGATCCGGAAAATGCGTGAGGCTGTGCTCACATTAACAGAACCTCTCGGTTCGGAAAGAA


if __name__ == "__main__":
    LCSM()
