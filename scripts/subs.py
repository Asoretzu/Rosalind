from services import fasta


def work(file_name):
    """Finding a Motif in DNA"""

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split()

    dataset = data[0]
    motif = data[1]

    length = len(motif)
    count = []

    # Search for motifs in the dataset
    for i in range(0, len(dataset)):
        if motif == dataset[i:i+length]:
            count.append(i+1)

    print(" ".join(str(n) for n in count))
