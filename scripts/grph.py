from services import fasta


def work(file_name):
    """Overlap Graphs"""

    data = fasta.get(file_name)
    fasta_ids = data[0]
    fasta_codes = data[1]

    prefix = []
    suffix = []
    s = ""
    k = 3

    for set in fasta_codes:
        # Get the prefix values
        for i in range(0, k):
            s = s + set[i]
        prefix.append(s)
        s = ""

        # Get the suffix values
        for i in range(-1, (-1-k), -1):
            s = s + set[i]
        s = s[::-1]
        suffix.append(s)
        s = ""

    # Compare suffix whit prefix
    for i in range(0, len(suffix)):
        for j in range(0, len(prefix)):
            if suffix[i] == prefix[j]:
                if prefix[i] == prefix[j] and suffix[i] == suffix[j]:
                    pass
                else:
                    print("{} {}".format(fasta_ids[i], fasta_ids[j]))
