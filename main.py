#!/usr/bin/python

import sys

from scripts import *


# Main function with options
def main(args):
    try:
        if args[1] == 'dna':
            dna.dna(args[2])
        else:
            print(f"The module <{args[1]}> doesn't exist.")
    except:
        print('Invalid arguments received.')


# Call the function of the script
if __name__ == "__main__":
    args = len(sys.argv) - 1

    if args == 2:
            main(sys.argv)
    else:
        print(f'Invalid number of arguments. Expected 2, but received {args}.')
