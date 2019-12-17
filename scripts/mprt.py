import requests
import os
# Download the Requests Module, via "pip install requests".


def mprt(file_name):
    """
    Prints the given access ID and a list of locations in the protein string
    where the motif can be found.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Finding a Protein Motif

    To allow for the presence of its varying forms, a protein motif is
    represented by a shorthand as follows:
    [XY] means "either X or Y"
    {X} means "any amino acid except X."
    For example, the N-glycosylation motif is written as N{P}[ST]{P}.

    You can see the complete description and features of a particular protein
    by its access ID "uniprot_id" in the UniProt database, by inserting the ID
    number into http://www.uniprot.org/uniprot/uniprot_id

    Alternatively, you can obtain a protein sequence in FASTA format by
    following:

    http://www.uniprot.org/uniprot/uniprot_id.fasta

    For example, the data for protein B5ZC00 can be found at
    http://www.uniprot.org/uniprot/B5ZC00.

    Given: At most 15 UniProt Protein Database access IDs.

    Return: For each protein possessing the N-glycosylation motif, output its
    given access ID followed by a list of locations in the protein string where
    the motif can be found.

    Sample Dataset
    A2Z669
    B5ZC00
    P07204_TRBM_HUMAN
    P20840_SAG1_YEAST

    Sample Output
    B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614
    """

    dataset = []

    with open(file_name, mode="r") as f:
        for line in f:
            dataset.append(line[0:-1])

    for file in dataset:
        url = "https://www.uniprot.org/uniprot/{}.fasta".format(file)
        r = requests.get(url)
        filename = url.split('/')[-1]
        with open(filename, 'wb') as output_file:
            output_file.write(r.content)

        data = ""
        with open("{}.fasta".format(file), mode="r") as f:
            for line in f:
                if line[0] != ">":
                    data = data + line[0:-1]

        # N-glycosylation motif is N{P}[ST]{P}
        motif = []
        for i in range(0, len(data)-2):
            if data[i] == "N" and data[i+1] != "P"\
                    and (data[i+2] == "S" or data[i+2] == "T")\
                    and data[i+3] != "P":
                motif.append(i+1)

        if len(motif) > 0:
            print(file)
            print(' '.join(map(str, motif)))

        os.remove("{}.fasta".format(file))
