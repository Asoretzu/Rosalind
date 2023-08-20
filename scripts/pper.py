from services import fasta


def work(file_name):
    """Partial Permutations"""

    data = fasta.get(file_name)
    data = data.split()

    n = int(data[0])
    k = int(data[1])
    perms = 1

    for i in range(k):
        perms = perms * (n-i)

    total = perms % 1000000

    print(total)
