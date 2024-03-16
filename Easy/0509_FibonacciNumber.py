def fib(self, n):
    # Base case check
    if n < 2:
        return n
    # Go from 2 to n and return what x becomes, adding y to it as we move up
    x, y = 0, 1
    for i in range(2, n + 1):
        x = x + y
        if n == i:
            return x
        x, y = y, x
    return -1
