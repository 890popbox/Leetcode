def largestAltitude(gain):
    # Variable to hold the output and the current altitude, then scan in O(N)
    output, curr = 0, 0
    for i in gain:
        curr += i
        output = max(output, curr)
    return output
