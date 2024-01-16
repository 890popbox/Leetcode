def reverseBits(self, n):
    rev = 0
    # Create the new number and go through all 32 bits of the given number
    for _ in range(0, 32):
        # Left shift the reversed number and add the last bit to it if needed (& does this simply)
        rev = (rev << 1) + (n & 1)
        # Shift original number right until we get to the last bit
        n >>= 1
    return rev
