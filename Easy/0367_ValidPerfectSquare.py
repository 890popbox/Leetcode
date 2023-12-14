def isPerfectSquare(self, num):
    # Create a start and end for a binary search type algorithm
    start, end = 1, num
    while start <= end:
        mid = (start + end + 1) // 2
        sqt = mid * mid
        # If the sqt is less than the original number, move the starting pos up
        # If the sqt is greater than the original number, move the ending position down
        # If neither of these than sqt==num, so return True
        if sqt < num:
            start = mid + 1
        elif sqt > num:
            end = mid - 1
        else:
            return True
    # If we never return True, and start<=end is met, return False, the answer must be a decimal
    return False
