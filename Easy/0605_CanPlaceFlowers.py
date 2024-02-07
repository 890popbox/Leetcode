def canPlaceFlowers(self, flowerbed, n):
    # If theres no flowers to lay
    if n == 0: return True
    empty = 1
    count = 0
    # If there exists a flower, increase the count for every position a flower can exist in between each other
    for bed in flowerbed:
        if bed:
            count += (empty - 1) // 2
            empty = 0
        else:
            empty += 1
    # If we end with at least two empty spots we can place a flower or more
    # Return True if we were able to lay N flowers or more
    count += empty // 2
    return count >= n
