from services import fasta


def work(file_name):
    """Consensus and Profile"""

    data = fasta.get(file_name)
    codes = data[1]

    a = 0
    c = 0
    g = 0
    t = 0

    total_a = ["A:", ]
    total_c = ["C:", ]
    total_g = ["G:", ]
    total_t = ["T:", ]

    # Get the number of every base in a given string
    for i in range(0, len(codes[0])):
        for line in codes:
            if line[i] == "A":
                a = a + 1
            elif line[i] == "C":
                c = c + 1
            elif line[i] == "G":
                g = g + 1
            elif line[i] == "T":
                t = t + 1

        total_a.append(a)
        a = 0
        total_c.append(c)
        c = 0
        total_g.append(g)
        g = 0
        total_t.append(t)
        t = 0

    consensus = ""
    a = 0
    c = 0
    g = 0
    t = 0

    # Get the consensus string (the most common base in a given position)
    for i in range(1, len(total_a)):
        value = max(total_a[i], total_c[i], total_g[i], total_t[i])

        if value == total_a[i]:
            consensus = consensus + "A"
        elif value == total_c[i]:
            consensus = consensus + "C"
        elif value == total_g[i]:
            consensus = consensus + "G"
        elif value == total_t[i]:
            consensus = consensus + "T"

    print(consensus)
    print(' '.join(map(str, total_a)))
    print(' '.join(map(str, total_c)))
    print(' '.join(map(str, total_g)))
    print(' '.join(map(str, total_t)))
