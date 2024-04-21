def isPowerOfThree(self, n):
    if n < 1: return False
    val = log10(n) / log10(3)
    return val == int(val)