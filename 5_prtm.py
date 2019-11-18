# ID = "PRTM"
# PROJECT = "Calculating Protein Mass"

# In a weighted alphabet, every symbol is assigned a positive real number called
# a weight. A string formed from a weighted alphabet is called a weighted string,
# and its weight is equal to the sum of the weights of its symbols.

# The standard weight assigned to each member of the 20-symbol amino acid
# alphabet is the monoisotopic mass of the corresponding amino acid.

# Given: A protein string P of length at most 1000 aa.

# Return: The total weight of P.

# Sample Dataset
# SKADYEK

# Sample Output
# 821.392

# A   71.03711
# C   103.00919
# D   115.02694
# E   129.04259
# F   147.06841
# G   57.02146
# H   137.05891
# I   113.08406
# K   128.09496
# L   113.08406
# M   131.04049
# N   114.04293
# P   97.05276
# Q   128.05858
# R   156.10111
# S   87.03203
# T   101.04768
# V   99.06841
# W   186.07931
# Y   163.06333


# file_name = "TXT/lalo.txt"
file_name = "TXT/rosalind_prtm.txt"


def amino_mass(amino):
    if amino == "A":
        return 71.03711
    if amino == "C":
        return 103.00919
    if amino == "D":
        return 115.02694
    if amino == "E":
        return 129.04259
    if amino == "F":
        return 147.06841
    if amino == "G":
        return 57.02146
    if amino == "H":
        return 137.05891
    if amino == "I":
        return 113.08406
    if amino == "K":
        return 128.09496
    if amino == "L":
        return 113.08406
    if amino == "M":
        return 131.04049
    if amino == "N":
        return 114.04293
    if amino == "P":
        return 97.05276
    if amino == "Q":
        return 128.05858
    if amino == "R":
        return 156.10111
    if amino == "S":
        return 87.03203
    if amino == "T":
        return 101.04768
    if amino == "V":
        return 99.06841
    if amino == "W":
        return 186.07931
    if amino == "Y":
        return 163.06333


def PRTM(dataset):
    mass = 0
    for amino in dataset:
        mass = mass + amino_mass(amino)

    print(round(mass, 3))


if __name__ == "__main__":
    dataset = ""
    # dataset = "SKADYEK"

    with open(file_name, mode="r") as f:
        for line in f:
            dataset = dataset + line[0:-1]

    PRTM(dataset)
