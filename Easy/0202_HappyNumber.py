def isHappy(self, n):
    # helper function that returns the sum of the sqt of digits in the number
    def sumSquares(x):
        summ = 0
        while x > 0:
            digit = x % 10
            summ += digit ** 2
            x /= 10
        return summ

    # keep a set of values, once they start repeating we return false
    values = set()
    # if n is ever 1, end loop and return True
    # otherwise add n to our set of values, get the sum of squares and continue
    # return False if we seen this value before, this means we will never see 1
    while n != 1:
        values.add(n)
        n = sumSquares(n)
        if n in values:
            return False
    return True
