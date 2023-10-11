def mySqrt(x):
    # Base case is if it's already under two, the middle search won't work
    if x < 2:
        return x
    # Binary Search Range, 0 to the number
    start, end = 0, x
    # The absolute difference of these will get closer to one the farther we go
    # Once this happens we can just return whatever start becomes because we are flooring the value.
    while abs(start-end) != 1:
        mid = (start+end) // 2
        # If mid sqrt is equal to what we want
        if mid*mid == x:
            return mid
        # Get closer to the correct side, if its greater making the end mid pushes it to the left and vice versa
        if mid*mid > x:
            end = mid
        else:
            start = mid
    # At this point we have returned an exact value or haven't found an exact value so start should be the closest
    return start
