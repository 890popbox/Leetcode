def commonFactors(self, a, b):
    # function to find the gcd
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return abs(x)

    gcd = gcd(a, b)
    output = 1
    # we only have to run this loop up to the gcd and can assume one is a common factor
    for i in range(2, gcd + 1):
        if gcd % i == 0:
            output += 1
    return output
# one is always a common factor and in a few cases can be the greatest factor
