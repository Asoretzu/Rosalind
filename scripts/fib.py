from services import fasta


def fib(file_name):
    """Rabbits and Recurrence Relations"""

    data = fasta.get(file_name)
    data = data.split()

    n = int(data[0])
    k = int(data[1])

    print(data)

    rabits = 0
    youngs = 0
    litter = 1

    for i in range(0, n-1):
        rabits = rabits + youngs
        youngs = litter
        litter = rabits * k

    print(rabits + youngs + litter)
