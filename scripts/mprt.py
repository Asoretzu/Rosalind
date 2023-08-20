import requests
import os
# Download the Requests Module, via "pip install requests".


def work(file_name):
    """Finding a Protein Motif"""

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
