from services import fasta


def fibd(file_name):
    """
    Prints the number of pairs of rabbits that will remain after n-th months.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Mortal Fibonacci Rabbits

    Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
    Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed
    that each pair of rabbits reaches maturity in one month and produces a
    single pair of offspring (one male, one female) each subsequent month.

    Our aim is to somehow modify this recurrence relation to achieve a dynamic
    programming solution in the case that all rabbits die out after a fixed
    number of months. See Figure 4 for a depiction of a rabbit tree in which
    rabbits live for three months (meaning that they reproduce only twice
    before dying).

    Given: Positive integers n≤100 and m≤20.

    Return: The total number of pairs of rabbits that will remain after the
    n-th month if all rabbits live for m months.

    Sample Dataset
    6 3

    Sample Output
    4
    """

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
