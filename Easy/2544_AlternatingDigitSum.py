def alternateDigitSum(n):
    # output, reverse, flag
    o, r, f = 0, 0, 1
    # Reverse the integer
    while n > 0:
        r *= 10
        r += (n - 10 * (n // 10))
        n //= 10
    # Go through the reversed integer
    while r > 0:
        # Method to get the modulus without %
        o += f * (r - 10 * (r // 10))
        f *= -1  # Alternate the flag each time
        r //= 10  # Divide the number until we get to zero
    return o

# There are a few ways to do this, reversing the number, using logs to get the length of the integer, etc
# I feel this one is simple to understand, short and simple to read.

