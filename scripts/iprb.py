from services import fasta


def work(file_name):
    """Mendel's First Law"""

    data = fasta.get(file_name)
    data = data.split()

    d = int(data[0])
    h = int(data[1])
    r = int(data[2])

    total = d + h + r

    r_r = (r / total) * ((r - 1) / (total - 1))
    h_h = (h / total) * ((h - 1) / (total - 1))
    h_r = (h / total) * (r / (total - 1)) + (r / total) * (h / (total - 1))
    r_total = r_r + (h_h * 0.25) + (h_r * 0.5)

    prob = 1 - r_total

    print("{}".format(round(prob, 5)))
