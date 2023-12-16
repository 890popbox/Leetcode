def findFinalValue(self, nums, original):
    d = {}
    # Create a dictionary, O(N)
    for n in nums:
        if n not in d:
            d[n] = 1
    # Multiply original until number doesn't exist in d, constant lookups until number doesn't exist
    while original in d:
        original *= 2
    return original
# Leetcode is okay with looking into the nums, weird cause it has to do a lookup each time.
