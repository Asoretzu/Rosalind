from services import fasta
from services import extras


def sseq(file_name):
    """Finding a Spliced Motif"""

    data = fasta.get(file_name)
    string = data[1][0]
    subseq = data[1][1]

    finds = []
    pos = 0

    for i in range(len(subseq)):
        for j in range(len(string)):
            if subseq[i] == string[j]:
                if j > pos:
                    finds.append(j+1)
                    pos = j
                    break

    extras.fancy_print(finds)
