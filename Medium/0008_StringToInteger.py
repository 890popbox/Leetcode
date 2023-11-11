def myAtoi(s):
    # Variables for the output, flag if negative or positive, and the index we are viewing
    output, flag, index = 0, 1, 0
    # Skip white spaces, do not go out of bounds
    while index < len(s) and s[index] == ' ':
        index += 1
    # All characters are whitespace or string does not exist
    if index == len(s):
        return 0
    # Check for positive or negative
    if s[index] == '+':
        index += 1
    elif s[index] == "-":
        index += 1
        flag = -1
    # Read the number and return output
    while index < len(s) and '9' >= s[index] >= '0':
        output *= 10
        output += int(s[index])
        index += 1
    return max(min(output * flag, 2 ** 31 - 1), -2 ** 31)  # Check for integer overflow
