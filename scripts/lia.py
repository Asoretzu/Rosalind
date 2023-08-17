from services import fasta
from services.math import fact


def lia(file_name):
    """Independent Alleles"""

    data = fasta.get(file_name)
    data = data.split()

    k = int(data[0])
    N = int(data[1])

    r = 2**k
    total = 0

    for i in range(N, r+1):
        prob = (fact(r) / (fact(i) * fact(r - i))) * (0.25**i) * (0.75**(r-i))
        total = total + prob

    print(round(total, 3))
