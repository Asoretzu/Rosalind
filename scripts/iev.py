from services import fasta


def work(file_name):
    """Calculating Expected Offspring"""

    data = fasta.get(file_name)
    data = data.split()

    c1 = int(data[0]) * 2
    c2 = int(data[1]) * 2
    c3 = int(data[2]) * 2
    c4 = int(data[3]) * 2
    c5 = int(data[4]) * 2
    c6 = int(data[5]) * 2

    # Get the average of offspring
    average = c1 + c2 + c3 + (c4 * 0.75) + (c5 * 0.5) + (c6 * 0)

    print(round(average, 1))
