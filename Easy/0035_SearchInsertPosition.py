def searchInsert(nums, target):
    # In a short array linear searching would work great
    # However as the array gets longer that may take a longer time
    # We will implement a binary search to deal with this
    start = 0
    end = len(nums) - 1
    # While the start is less than or equal to end, if it ever passes this is where the target should be located.
    while start <= end:
        index = (start + end) // 2  # First instance of index is the middle of our array
        # If the target is greater than the number we are looking at, we must go right
        if target > nums[index]:
            start = index + 1
        # If the target is less than the number we are looking at, we must go left
        elif target < nums[index]:
            end = index - 1
        # If both the conditions are not true, nums[index] must be target
        else:
            return index
    return start
