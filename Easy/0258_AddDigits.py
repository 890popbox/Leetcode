    def addDigits(self, num):
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num

# If the number is under 10, it's already one digit, return it
# Otherwise add all the digits to the total/sum, replace num with it
# This will repeat until the number is under 10, meaning it is 0 to 9
