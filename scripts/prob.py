from services import fasta
from math import log10
from services import extras


def prob(file_name):
    """
    An array is a structure containing an ordered collection of objects
    (numbers, strings, other arrays, etc.). We let A[k] denote the k-th value
    in array A. You may like to think of an array as simply a matrix having
    only one row.

    A random string is constructed so that the probability of choosing each
    subsequent symbol is based on a fixed underlying symbol frequency.

    GC-content offers us natural symbol frequencies for constructing random DNA
    strings. If the GC-content is x, then we set the symbol frequencies of C
    and G equal to x/2 and the symbol frequencies of A and T equal to (1−x)/2.
    For example, if the GC-content is 40%, then as we construct the string, the
    next symbol is 'G'/'C' with probability 0.2, and the next symbol is 'A'/'T'
    with probability 0.3.

    In practice, many probabilities wind up being very small. In order to work
    with small probabilities, we may plug them into a function that "blows them
    up" for the sake of comparison. Specifically, the common logarithm of x
    (defined for x>0 and denoted log10(x)) is the exponent to which we must
    raise 10 to obtain x.

    The common logarithm function y=log10(x), of x-values between 0 and 1
    always winds up mapping to y-values between −∞ and 0: x-values near 0 have
    logarithms close to −∞, and x-values close to 1 have logarithms close to 0.
    Thus, we will select the common logarithm as our function to "blow up"
    small probability values for comparison.

    Given: A DNA string s of length at most 100 bp and an array A containing at
    most 20 numbers between 0 and 1.

    Return: An array B having the same length as A in which B[k] represents the
    common logarithm of the probability that a random string constructed with
    the GC-content found in A[k] will match s exactly.

    Sample Dataset
    ACGATACAA
    0.129 0.287 0.423 0.476 0.641 0.742 0.783

    Sample Output
    -5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009
    """

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split("\n")

    string = data[0]
    d = data[1].split()
    array = []

    for i in range(len(d)):
        array.append(float(d[i]))

    at_count = 0
    gc_count = 0

    for i in range(len(string)):
        if string[i] == "G" or string[i] == "C":
            gc_count += 1
        elif string[i] == "A" or string[i] == "T":
            at_count += 1

    logs = []

    for n in array:
        log1 = (n / 2) ** gc_count
        log2 = ((1-n) / 2) ** at_count

        logs.append(round(log10(log1) + log10(log2), 3))

    extras.fancy_print(logs)
