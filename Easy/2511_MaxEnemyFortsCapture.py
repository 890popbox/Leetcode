def captureForts(forts):
    # Create a variable for the output, and another to keep track of the starting point
    output, start = 0, 0
    # The ending point will increase in linear time O(N) as we scan through the list of forts
    for end in range(0, len(forts)):
        # If our start and end are not zero, and they are not the same fort, we can check the distance between them
        # No need for absolute value here as the end should always be greater than the start
        if forts[start] != 0 and forts[end] != 0 and forts[start] != forts[end]:
            output = max(output, end - start - 1)
        # If the spot we are viewing is not an enemy tower, it is either friendly or open
        # Both have to be considered, if ever start==end the top statement just won't consider it vaible
        if forts[end] != 0:
            start = end
    # This is similiar to marking friendly/empty towers, comparing distance between them
    # And then reseting either the friendly or empty tower variable based off the tower we are viewing
    # This uses less variables and organizing comparisons into two simple ifs
    return output