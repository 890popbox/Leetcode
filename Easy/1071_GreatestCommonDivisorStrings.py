def gcdOfStrings(self, str1, str2):
    # Check if the strings match forward and backwards, if they do not return an empty string
    if str1 + str2 != str2 + str1:
        return ""

    # euclidean gcd algo
    def euc(x, y):
        while (y):
            x, y = y, x % y
        return abs(x)

    # Get the gcd and return either string, up to that length, that will be our result
    gcd = euc(len(str1), len(str2))
    return str1[:gcd]
