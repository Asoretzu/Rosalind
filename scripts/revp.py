from services import fasta
from services import translate


def revp(file_name):
    """Locating Restriction Sites"""

    dataset = fasta.get(file_name)
    pairs = dataset[1]

    for i in range(4, 13):

        for j in range(0, len(pairs)):
            p = pairs[j: j+i]

            if len(p) < i:
                break

            r_p = p[::-1]

            r = translate.complement(r_p)

            if p == r:
                print("{} {}".format(j+1, len(p)))
