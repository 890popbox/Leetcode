import math


def numberOfWays(startPos, endPos, k):
    # Math way to solve, if start-end-steps mod 2 is not 0, we will never reach end in k steps
    if (startPos - endPos - k) % 2:
        return 0
    # Otherwise we are able to get a number greater than 
    # The answer may be very large, return mod 10^9 + 7 to avoid this.
    # n! / (k! * (n – k)!) is the combination formula that to choose
    # k items from n items without repetition and without order.
    # Below, our k == n and our c == k
    c = (endPos - startPos + k) // 2
    return math.factorial(k) / (math.factorial(c) * math.factorial(abs(k - c))) % (10 ** 9 + 7)

# Originally I solved this using a decision tree, this is extremely slow and starts using a lot of space
# Dynamic programming helps improve this, however this is the most efficient solution as it uses Math
# This is not very intuitive at all, it involves use of the combination formula
