#!/usr/bin/python

import sys
import importlib

import scripts

# Main function with options
def main(args):
    try:
        if args[1] in scripts.__all__:
            module = importlib.import_module("scripts." + args[1])
            module.work("txt/rosalind_" + args[1] + ".txt")
        else:
            print(f"The module '{args[1]}' doesn't exist.")
    except:
        print('Invalid arguments received.')


# Call the function of the script
if __name__ == "__main__":
    args = len(sys.argv) - 1

    if args == 1:
            main(sys.argv)
    else:
        print(f'Invalid number of arguments. Expected 1, but received {args}.')
