from services import fasta
from math import factorial


def work(file_name):
    """Independent Alleles"""

    data = fasta.get(file_name)
    data = data.split()

    k = int(data[0])
    N = int(data[1])

    r = 2**k
    total = 0

    for i in range(N, r+1):
        prob = (factorial(r) / (factorial(i) * factorial(r - i))) * (0.25**i) * (0.75**(r-i))
        total = total + prob

    print(round(total, 3))
