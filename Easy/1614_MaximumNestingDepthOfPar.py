def maxDepth(s):
    # Two variables to store a count, one is the final output, the other is the count
    count, output = 0, 0
    # Scan the string, ( is +1, ) is -1
    for c in s:
        # If left para, increase it and store the new max if it is greater
        if c == "(":
            count += 1
            output = max(output, count)
        # If right para, subtract it, no need to check for new max here
        if c == ")":
            count -= 1
    # Every other character is not counted and final result is returned
    return output
