from services import fasta
from math import log10
from services import extras


def prob(file_name):
    """Introduction to Random Strings"""

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split("\n")

    string = data[0]
    d = data[1].split()
    array = []

    for i in range(len(d)):
        array.append(float(d[i]))

    at_count = 0
    gc_count = 0

    for i in range(len(string)):
        if string[i] == "G" or string[i] == "C":
            gc_count += 1
        elif string[i] == "A" or string[i] == "T":
            at_count += 1

    logs = []

    for n in array:
        log1 = (n / 2) ** gc_count
        log2 = ((1-n) / 2) ** at_count

        logs.append(round(log10(log1) + log10(log2), 3))

    extras.fancy_print(logs)
