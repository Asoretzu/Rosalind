from services import fasta


def work(file_name):
    """Completing a Tree"""

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split("\n")
    n = int(data[0])
    data = data[1:-1]

    edges = n - 1 - len(data)

    print(edges)
