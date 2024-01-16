def hammingWeight(self, n):
    count = 0
    # Scan all bits of current number, shifting right each time until finish, add if it exists
    while n:
        if n & 1:
            count += 1
        n >>= 1
    return count
