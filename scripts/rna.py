# ID = "RNA"
# PROJECT = "Transcribing DNA into RNA"

# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G',
# and 'U'.

# Given a DNA string "t" corresponding to a coding strand, its transcribed RNA
# string "u" is formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string "t" having length at most 1000 nt.

# Return: The transcribed RNA string of t.

# Sample Dataset
# GATGGAACTTGACTACGTAAATT

# Sample Output
# GAUGGAACUUGACUACGUAAAUU


def RNA():
    dna = "GATGGAACTTGACTACGTAAATT"
    rna = ""

    for nt in dna:
        if nt == "T":
            rna = rna + "U"
        else:
            rna = rna + nt

    print(rna)


if __name__ == "__main__":
    RNA()
