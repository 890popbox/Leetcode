def distributeCandies(self, n, limit):
    # If we can't distribute all candies without going over the limit return zero
    if n > limit * 3: return 0
    count = 0
    # Brute force two loop method, Both two people can only have candies upto limit
    # The unknown value must be between 0 and the limit (inclusive), count if so
    for i in range(0, limit + 1):
        for j in range(0, limit + 1):
            if 0 <= n - i - j <= limit:
                count += 1
    return count
