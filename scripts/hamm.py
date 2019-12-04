# ID = "HAMM"
# PROJECT = "Counting Point Mutations"


# Given two strings s and t of equal length, the Hamming distance between s and
# t, denoted dH(s,t), is the number of corresponding symbols that differ in s
# and t.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output
# 7


from services import fasta


def hamm(file_name):
    data = fasta.get(file_name, remove_new_line=False)
    data = data.split()

    code1 = data[0]
    code2 = data[1]
    length = len(code1)

    mutations = 0

    for i in range(0, length):
        if code1[i] != code2[i]:
            mutations = mutations + 1

    print(mutations)
