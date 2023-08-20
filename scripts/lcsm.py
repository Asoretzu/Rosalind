from services import fasta


def work(file_name):
    """Finding a Shared Motif"""

    dataset = fasta.get(file_name)
    dataset = sorted(dataset[1], key=len)
    seq = dataset[1:]
    srtd_seq = sorted(seq, key=len)

    short_seq = srtd_seq[0]
    comp_seq = srtd_seq[1:]
    motif = ""

    for i in range(len(short_seq)):
        for j in range(i, len(short_seq)):
            m = short_seq[i: j+1]
            shared_motif = False

            for seq in comp_seq:
                if m in seq:
                    shared_motif = True
                else:
                    break

            if shared_motif and len(m) > len(motif):
                motif = m

    print(motif)
