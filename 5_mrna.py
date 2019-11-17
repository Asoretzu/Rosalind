# ID = "MRNA"
# PROJECT = "Inferring mRNA from Protein"

# For positive integers a and n, a modulo n (written amodn in shorthand) is the
# remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

# Modular arithmetic is the study of addition, subtraction, multiplication, and
# division with respect to the modulo operation. We say that a and b are
# congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

# Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn,then
# a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you
# may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

# As you will see in this exercise, some Rosalind problems will ask for a (very
# large) integer solution modulo a smaller number to avoid the computational
# pitfalls that arise with storing such large numbers.

# Given: A protein string of length at most 1000 aa.

# Return: The total number of different RNA strings from which the protein could
# have been translated, modulo 1,000,000. (Don't neglect the importance of the
# stop codon in protein translation.)

# Sample Dataset
# MA

# Sample Output
# 12


def get_protein():
    dataset = ""
    with open("TXT/rosalind_mrna.txt", mode="r") as f:
        for line in f:
            dataset = dataset + line[0:-1]

    return dataset


def aminos(amino):
    if amino == "A":
        return 4
    if amino == "C":
        return 2
    if amino == "D":
        return 2
    if amino == "E":
        return 2
    if amino == "F":
        return 2
    if amino == "G":
        return 4
    if amino == "H":
        return 2
    if amino == "I":
        return 3
    if amino == "K":
        return 2
    if amino == "L":
        return 6
    if amino == "M":
        return 1
    if amino == "N":
        return 2
    if amino == "P":
        return 4
    if amino == "Q":
        return 2
    if amino == "R":
        return 6
    if amino == "S":
        return 6
    if amino == "T":
        return 4
    if amino == "V":
        return 4
    if amino == "W":
        return 1
    if amino == "Y":
        return 2


def MRNA(dataset):
    a = 1

    for amino in dataset:
        a = a * aminos(amino)

    # Add the Stop codon
    a = a * 3

    print(a % 1000000)


if __name__ == "__main__":

    dataset = get_protein()

    MRNA(dataset)
