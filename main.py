#!/usr/bin/python

import sys

from scripts import *


# Main function with options
def main(work):
    try:
        if work[1] == 'dna':
            print(dna.dna(work[2]))
        else:
            print(f"The module <{work[1]}> doesn't exist.")
    except:
        print('Invalid arguments received.')


# Call the function of the script
if __name__ == "__main__":
    args = len(sys.argv) - 1

    if args == 2:
            main(sys.argv)
    else:
        print(f'Invalid number of arguments. Expected 2, but received {args}.')
