from services import fasta


# Search for the longest increasing subsequence
def _increasing(data, length):
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
def _decreasing(data, length):
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
def _print_data(data):
    d = []
    for i in data:
        d.append(str(i))

    print(" ".join(map(str, d)))


# Gets the data and calls all the functions
def work(file_name):
    """Longest Increasing Subsequence"""

    string = ""
    data = []
    increase = []
    decrease = []

    string = fasta.get(file_name, remove_new_line=False)

    string = string.split()
    length = int(string[0])
    string = string[1:]

    for element in string:
        data.append(int(element))

    increase = _increasing(data, length)
    decrease = _decreasing(data, length)

    _print_data(increase)
    _print_data(decrease)
