# ID = ""
# PROJECT = ""

# A DNA string is a reverse palindrome if it is equal to its reverse
# complement. For instance, GCATGC is a reverse palindrome because its reverse
# complement is GCATGC. See Figure 2.

# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string
# having length between 4 and 12. You may return these pairs in any order.

# Sample Dataset

# >Rosalind_24
# TCAATGCATGCGGGTCTATATGCAT

# Sample Output

# 4 6
# 5 4
# 6 6
# 7 4
# 17 4
# 18 4
# 20 6
# 21 4


from services import fasta


def translate(r_p):
    t = ""

    for i in range(0, len(r_p)):
        if r_p[i] == "A":
            t = t + "T"
        elif r_p[i] == "T":
            t = t + "A"
        elif r_p[i] == "G":
            t = t + "C"
        elif r_p[i] == "C":
            t = t + "G"
    return t


def REVP():
    # dataset = fasta.get("TXT/lalo.txt")
    dataset = fasta.get("TXT/rosalind_revp.txt")
    pairs = dataset[1]

    for i in range(4, 13):

        for j in range(0, len(pairs)):
            p = pairs[j: j+i]

            if len(p) < i:
                break

            r_p = p[::-1]

            r = translate(r_p)

            if p == r:
                print("{} {}".format(j+1, len(p)))


if __name__ == "__main__":
    REVP()
