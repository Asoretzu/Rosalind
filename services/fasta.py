# Get function for single or multiple strings, with or without IDs
def get(file_name, remove_new_line=True):
    fasta_ids = []
    fasta_codes = []
    string = ""

    # Open the file and parsing every string
    with open(file_name, mode="r") as f:
        for line in f:
            # Check for FASTA IDs
            if line[0] == ">":
                line = line[1: -1]
                fasta_ids.append(line)

                # Asign every FASTA code
                if len(fasta_ids) == 1:
                    pass
                else:
                    fasta_codes.append(string)
                    string = ""
            else:
                # Concatenate all the FASTA code
                if remove_new_line:
                    string = string + line[0:-1]
                else:
                    string = string + line

        # Asign the last FASTA code
        fasta_codes.append(string)

    if not fasta_ids:
        # Return the code in a string
        return fasta_codes[0]
    if len(fasta_ids) == 1:
        # Return the ID and code in a list
        return [fasta_ids[0], fasta_codes[0]]
    # Return IDs and codes in two lists within a list
    return [fasta_ids, fasta_codes]
