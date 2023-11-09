def reverse(x):
    # Create variables to hold the reverse and a flag
    rev, flag = 0, 1
    # If negative, make it positive and turn the flag on
    if x < 0:
        x *= -1
        flag = -1
    # Go until zero number is gone, and rev is the reversed number
    while x > 0:
        rev *= 10
        rev += x % 10
        x //= 10
    # Set the number back to negative if it was negative
    output = rev * flag
    # Check if the value is within the constraints
    return output if (2 ** 31 - 1) > output > (-2 ** 31) else 0