def canJump(self, nums):
    last_index = len(nums) - 1
    # Scan backwards from the second to last index
    for i in range(last_index - 1, -1, -1):
        # If this index has a jump count which goes to the last index or beyond
        if i + nums[i] >= last_index:
            # Update because we can just use this to reach the last index
            last_index = i
    # If we can reach the end with the first position, True will be returned
    return last_index == 0
