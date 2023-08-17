from services import fasta


def gc(file_name):
    """Computing GC Content"""

    data = fasta.get(file_name)

    fasta_ids = data[0]
    fasta_codes = data[1]

    pair_count = []
    gc_content = []

    # Search for every C and G letter in a FASTA CODE
    for codes in fasta_codes:
        count = 0
        for i in range(0, len(codes)):
            code = codes[i]
            if code == "G" or code == "C":
                count = count + 1
        pair_count.append(count)

    # Get the GC CONTENT (%) of G's and C's
    for i in range(0, len(fasta_ids)):
        porcent = ((100 / len(fasta_codes[i])) * pair_count[i])
        gc_content.append(porcent)

    high = max(gc_content)

    # Print the result
    for i in range(0, len(fasta_ids)):
        if gc_content[i] == high:
            print("{}\n{}".format(fasta_ids[i], round(gc_content[i], 6)))
            break
