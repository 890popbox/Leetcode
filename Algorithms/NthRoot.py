import math


# Creating an NthRoot function based on the Sqrt one but we can provide our own N
def NthRoot(n_, nth_):
    # Anything to the 0 root or square is 1
    if nth_ == 0:
        return 1
    # Negative checking flag
    negative = True if nth_ < 0 else False
    # Create some kind of range for binary search, start and end
    start, end = 0, n_
    e = 0.000001  # Precision level, if possible (this case is 6 digits
    while start <= end:
        mid = (start + end) / 2
        tmp = 1
        if nth_ > 2:
            for i in range(0, nth_):
                tmp *= mid
        else:
            tmp = mid * mid

        error = abs(tmp - n_)

        # Result found
        if error <= e:
            # If negative its 1 divided by the result, otherwise its the result
            if negative:
                return 1 / mid
            return mid

        if tmp > n_:
            end = mid
        else:
            start = mid


print(math.sqrt(146166451536112562))
print(NthRoot(146166451536112562, 2))
# 12, 1, 0.083
print(NthRoot(144, 2))
print(NthRoot(144, 0))
print(NthRoot(144, -2))
