from services import fasta


def work(file_name):
    """Counting Point Mutations"""

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split()

    code1 = data[0]
    code2 = data[1]
    length = len(code1)

    mutations = 0

    for i in range(0, length):
        if code1[i] != code2[i]:
            mutations = mutations + 1

    print(mutations)
