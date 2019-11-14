# ID = "FIB"
# PROJECT = "Rabbits and Recurrence Relations"

# A sequence is an ordered collection of objects (usually numbers), which are
# allowed to repeat. Sequences can be finite or infinite. Two examples are the
# finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers
# (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.

# A recurrence relation is a way of defining the terms of a sequence with
# respect to the values of previous terms. In the case of Fibonacci's rabbits
# from the introduction, any given month will contain the rabbits that were
# alive the previous month, plus any new offspring. A key observation is that
# the number of offspring in any month is equal to the number of rabbits that
# were alive two months prior. As a result, if Fn represents the number of
# rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence
# having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2
# (with F1=F2=1 to initiate the sequence). Although the sequence bears
# Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

# When finding the n-th term of a sequence defined by a recurrence relation, we
# can simply use the recurrence relation to generate terms for progressively
# larger values of n. This problem introduces us to the computational technique
# of dynamic programming, which successively builds up solutions by using the
# answers to smaller cases.

# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation, every pair of reproduction-age
# rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# Sample Dataset
# 5 3

# Sample Output
# 19


# def FIB(n, k):
#     rabits = 0
#     youngs = 2
#     litter = 0
#
#     for i in range(0, n + 1):
#
#         pairs = rabits // 2
#
#         rabits = rabits + youngs
#
#         youngs = litter
#         litter = pairs * k
#
#         print("Rabits: {}".format(rabits))
#         print("Youngs: {}".format(youngs))
#         print("Litter: {}".format(litter))
#         print("Total: {}".format(rabits + youngs + litter))
#         print("*" * 50)


def FIB(n, k):
    #if n == 1:
    #    return 1

    #elif n == 2:
    #    return k;

    for i in range(n, 0):
        oneGen = FIB(n, k)
        twoGen = FIB(n - 1, k)

    #if n <= 4:
    #    return oneGen + twoGen

        return oneGen + (twoGen * k)


if __name__ == "__main__":
    n = 5
    k = 3
    fib = FIB(n, k)
    print(fib)
