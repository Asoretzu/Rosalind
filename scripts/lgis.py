# ID = "LGIS"
# PROJECT = "Longest Increasing Subsequence"

# A subsequence of a permutation is a collection of elements of the permutation
# in the order that they appear. For example, (5, 3, 4) is a subsequence of
# (5, 1, 3, 4, 2).

# A subsequence is increasing if the elements of the subsequence increase, and
# decreasing if the elements decrease. For example, given the permutation
# (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a
# decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two
# subsequences are as long as possible.

# Given: A positive integer n≤10000 followed by a permutation π of length n.
#
# Return: A longest increasing subsequence of π, followed by a longest
# decreasing subsequence of π.

# Sample Dataset

# 5
# 5 1 4 2 3

# Sample Output

# 1 2 3
# 5 4 2


# file_name = "TXT/lalo.txt"
file_name = "TXT/rosalind_lgis.txt"


# Search for the longest increasing subsequence
def increasing(data, length):
    M = [None] * length
    P = [None] * length

    # Asign the first element of data
    L = 1
    M[0] = 0

    # Start searching from the second element
    for i in range(1, length):
        low = 0
        hi = L

        # Check the hi value
        if data[M[hi-1]] < data[i]:
            j = hi

        else:
            # Binary search
            while hi - low > 1:
                mid = (hi + low) // 2
                if data[M[mid-1]] < data[i]:
                    low = mid
                else:
                    hi = mid

            j = low

        P[i] = M[j-1]

        if j == L or data[i] < data[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Getting the result
    result = []
    pos = M[L-1]

    for i in range(0, L):
        result.append(data[pos])
        pos = P[pos]

    result = result[::-1]
    return result


# Search for the longest decreasing subsequence
def decreasing(data, length):
    M = [None] * length
    P = [None] * length

    # Asign the first element of data
    L = 1
    M[0] = 0

    # Start searching from the second element
    for i in range(1, length):
        low = 0
        hi = L

        # Check the low value
        if data[M[hi-1]] > data[i]:
            j = hi

        else:
            # Binary search
            while hi - low > 1:
                mid = (hi + low) // 2
                if data[M[mid-1]] > data[i]:
                    low = mid
                else:
                    hi = mid

            j = low

        P[i] = M[j-1]

        if j == L or data[i] > data[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Getting the result
    result = []
    pos = M[L-1]

    for i in range(0, L):
        result.append(data[pos])
        pos = P[pos]

    result = result[::-1]
    return result


# Print the subsequence in a fancy way
def print_data(data):
    d = []
    for i in data:
        d.append(str(i))

    print(" ".join(map(str, d)))


# Gets the data and calls all the functions
def LGIS():
    string = ""
    data = []
    increase = []
    decrease = []

    with open(file_name, mode="r") as f:
        for line in f:
            string = string + line

    string = string.split()
    length = int(string[0])
    string = string[1:]

    for element in string:
        data.append(int(element))

    increase = increasing(data, length)
    decrease = decreasing(data, length)

    print_data(increase)
    print_data(decrease)


if __name__ == "__main__":
    LGIS()
