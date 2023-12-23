def removeDuplicates(self, nums):
    # edge case
    if len(nums) < 3: return len(nums)
    # same as removing dups in place but moving forward by two
    c = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[c - 2]:
            nums[c] = nums[i]
            c += 1
    return c
