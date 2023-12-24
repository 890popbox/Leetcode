def minSubArrayLen(self, target, nums):
    # if the sum of our numbers is less than or equal to the target, handle this
    nsum = sum(nums)
    if nsum<target:
        return 0
    elif nsum==target:
        return len(nums)
    # hold the current highest length, max this can be is the array length, we can achive lower
    length = len(nums)
    left = 0
    total = 0
    # scan array adding up numbers until it becomes greater than or equal to the target
    for right in range(0, len(nums)):
        total+=nums[right]
        # if the total is greater or equal to target, save that length and remove from left
        while total>=target:
            length = min(length, right-left+1)
            total-=nums[left]
            left+=1
    return length
# if first base conditions are not met there must be a solution
# removing from where we came from takes all possible sub arrays into consideration
# and does not move forward until the total becomes less
