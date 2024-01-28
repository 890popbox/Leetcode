def jump(self, nums):
    # This solution is very similiar to Jump Game I, This time we must return a count
    if len(nums) == 1: return 0

    # current: ending index of current jump
    # next: ending index of next jump
    curr_end, nxt_end = 0, 0
    jumps = 0

    for i in range(0, len(nums)):
        # if the current index is out of current level, add one to go to next
        if i > curr_end:
            jumps += 1
            curr_end = nxt_end
        # update level and take the max jump we can
        nxt_end = max(nxt_end, i + nums[i])
        # exit early if we can't make it to the end, not needed because in this case there is an answer
        # if i>nxt_end: return -1
    return jumps

