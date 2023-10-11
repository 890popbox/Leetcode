# This has potential for more optimization
def addBinary(a, b):
    # Return everything the result as a binary string
    s, carry = [], 0

    # Two pointers to scan the binary strings
    i, j = len(a) - 1, len(b) - 1

    # Loop until both pointers reach the start of their strings and no carry exists
    while i >= 0 or j >= 0 or carry:

        # Add the current binary digit in string a, if the pointer is still within bounds
        if i >= 0:
            carry += int(a[i])
            i -= 1

        # Add the current binary digit in string b, if the pointer is still within bounds
        if j >= 0:
            carry += int(b[j])
            j -= 1
        s.append(str(carry % 2))
        carry //= 2
    # Reverse the result and create a string
    return ''.join(reversed(s))
