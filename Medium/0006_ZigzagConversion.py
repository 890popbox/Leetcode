def convert(s, numRows):
    # If there is only one row, that's just the string
    if numRows == 1:
        return s
    # Otherwise we have to write an algorithm to deal with the zig-zag shape they define in the problem
    # Store the output as an empty string and fill it as we go along
    output = []
    size, inc = len(s), (numRows - 1) * 2
    # Increment is how much we will move forward each time when dealing with the zig-zag
    # The extra character is located at (inc-2*r)
    # Go through each row, adding the correct position based off math
    # Step one, go through the first row
    for r in range(0, size, inc):
        output.append(s[r])
    # Step two, go through the middle rows
    for r in range(1, numRows - 1):
        for i in range(r, size, inc):
            # This is the character we are currently visiting
            output.append(s[i])
            extra = i + inc - (2 * r)
            # i is the position of the current item, move this up and subtract 2*r
            # This calculation depends on the rows position
            if extra < size:
                output.append(s[extra])
    # Step three, go through the last row
    for r in range(numRows - 1, size, inc):
        output.append(s[r])
    return ''.join(output)

# This could be done in one loop, this avoids many comparisons
# The time complexity is still O(N) and N is the length of string
# This is because we never revisit any same characters in the string
