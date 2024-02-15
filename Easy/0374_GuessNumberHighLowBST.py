def guessNumber(self, n):
    start, end = 1, n
    # binary search while start hasn't hit the end yet
    while start <= end:
        mid = (start + end) // 2
        pick = guess(mid)
        # If the answer is correct, exit early
        if pick == 0:
            return mid
        # My guess is too low, push the start to middle
        # Else my guess is too high, push the end to middle
        elif pick == 1:
            start = mid + 1
        else:
            end = mid - 1
    # If there is no a valid answer
    return -1
