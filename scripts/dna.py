"""Counting DNA Nucleotides."""

import matplotlib.pyplot as plt

from services import fasta

# DNA module: Counting and Plotting
def dna(file_name):
    try:
        dna = fasta.get(file_name)

        a, c, g, t = 0, 0, 0, 0

        for nt in dna:
            if nt == 'A':
                a += 1
            elif nt == 'C':
                c += 1
            elif nt == 'G':
                g += 1
            elif nt == 'T':
                t += 1
            else:
                print(f'Unknow element: {nt}.')

        counts = [a, c, g, t]

        # Prints the nucleotides count in the specified format
        print(" ".join(map(str, counts)))

        # Plotting the nucleotides count
        plt.bar(range(4), counts)
        plt.title('Counting DNA Nucleotides')
        plt.ylabel('Count')
        plt.xticks(range(len(counts)), ['A', 'C', 'G', 'T'])
        plt.show()

    except:
        print('Wrong information.')
