def findMiddleIndex(self, nums):
    # Hold the left and right sum
    left, right = 0, sum(nums)
    # Scan through the whole array
    for i in range(0, len(nums)):
        print(left, right, i)
        if left == right - nums[i]:
            return i
        left += nums[i]
        right -= nums[i]
    return -1
