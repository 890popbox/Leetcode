    def hammingDistance(self, x, y):
        c = 0
        while x or y:
            if x%2!=y%2:
                c+=1
            x/=2
            y/=2
        return c
# Hold the count and while x or y still exist, count if their remainders are different
