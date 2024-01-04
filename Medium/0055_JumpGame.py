# Scan from the start to end with possibly to reach end quicker than end to start, O(N)
def canJump(self, nums):
    if len(nums) == 1: return True
    jump, maxjump = 0, nums[0]
    index, last_index = 0, len(nums) - 1
    # index is able to reach maxJump or lower with current information given
    while index <= maxjump:
        # If the max we can jump ever reachs or passes the last_index this is True
        if maxjump >= last_index: return True
        # The farthest place we can get to jumping from current index, update maxJump if its greater than current
        jump = index + nums[index]
        if jump > maxjump: maxjump = jump
        index += 1
    return False


# Alternative option from end to start, O(N)
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
