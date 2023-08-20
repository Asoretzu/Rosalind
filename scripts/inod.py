def work(nodes):
    """Counting Phylogenetic Ancestors"""

    text = ""

    with open(nodes, "r") as file:
        for line in file:
            text += line
    
    print(int(text) - 2)
