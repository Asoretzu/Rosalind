from services import fasta


def work(file_name):
    """Counting DNA Nucleotides."""
    
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
                print(f'Unknow element: {nt}')

        counts = [a, c, g, t]

        # Prints the nucleotides count in the specified format
        print(" ".join(map(str, counts)))

    except:
        print('Wrong information.')
