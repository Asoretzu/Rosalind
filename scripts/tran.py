from services import fasta


def _trans_finder(b1, b2):
    transition = [["A", "G"], ["C", "T"]]

    for trans in transition:
        if b1 in trans and b2 in trans:
            return [1, 0]
    return[0, 1]


def work(file_name):
    """Transitions and Transversions"""

    data = fasta.get(file_name)
    str1 = data[1][0]
    str2 = data[1][1]

    transitions = 0
    transversions = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            trans = _trans_finder(str1[i], str2[i])
            transitions = transitions + trans[0]
            transversions = transversions + trans[1]

    print(round(transitions/transversions, 11))
