def climbStairs(n):
    # If there are no stairs, or one
    if n == 0 or n == 1:
        return 1
    # Otherwise there are stairs, let's count
    # We know you can just go up the stairs one step at a time so we start at one
    prev, curr = 1, 1
    # Go until the range is met, we start at 2 because 0-2 is stratified.
    """
    So for example with 4; 2 goes until 5.. How it updates each time below
    #2 tmp = 1, curr = 2, prev = 1
    #3 tmp = 2, curr = 3, prev = 2
    #4 tmp = 3, curr = 5, prev = 3
    """
    for i in range(2, n + 1):
        # Temp var to as a placeholder for when curr changes, using fib concept
        tmp = curr
        curr = prev + curr
        prev = tmp
    return curr