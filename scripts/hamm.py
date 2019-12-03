# ID = "HAMM"
# PROJECT = "Counting Point Mutations"


# Given two strings s and t of equal length, the Hamming distance between s and t,
# denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output
# 7


def HAMM():
    # code1 = "GAGCCTACTAACGGGAT"
    # code2 = "CATCGTAATGACGGCCT"
    dataset = []
    mutations = 0

    with open("TXT/rosalind_hamm.txt", mode="r") as f:
        for line in f:
            dataset.append(line[0:-1])

    code1 = dataset[0]
    code2 = dataset[1]
    length = len(code1)


    for i in range(0, length):
        if code1[i] != code2[i]:
            mutations = mutations + 1

    print(mutations)

if __name__ == "__main__":
    HAMM()
