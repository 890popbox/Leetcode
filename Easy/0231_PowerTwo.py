    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        while (n % 2 == 0):
            n /= 2
        return n == 1
# Base case if number is zero or less it must be false, 1 must be true
# Divide by zero, if there is ever a remainder its False, otherwise keep going
# return n==1
