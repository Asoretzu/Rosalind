from services import fasta


def fibd(file_name):
    """Mortal Fibonacci Rabbits"""

    data = fasta.get(file_name)
    data = data.split()

    n = int(data[0])
    m = int(data[1])

    offspring = 0

    pairs = []

    # This construct a vector m - 1
    for i in range(0, m-1):
        pairs.append(0)

    pairs.append(1)

    # Get the pairs of each month
    for i in range(0, n-1):
        for j in range(0, m-1):
            offspring = offspring + pairs[j]

        pairs.append(offspring)
        pairs.pop(0)
        offspring = 0

    # Get the sum of all the pairs
    total = 0
    for i in range(0, len(pairs)):
        total = total + pairs[i]

    print(total)
