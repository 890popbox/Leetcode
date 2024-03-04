    def isUgly(self, n):
        if n <= 0:
            return False

        while n % 2 == 0:
            n = n / 2
        while n % 3 == 0:
            n = n / 3
        while n % 5 == 0:
            n = n / 5

        return n == 1 

# Zero or less is False, then while the number is greater than 1 try each mod in order to see if they work
# Try all of the mods in order until n is not greater than one
# If by the end of all this n==1, then return True
