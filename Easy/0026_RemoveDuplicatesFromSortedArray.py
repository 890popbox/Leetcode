def removeDuplicates(self, nums):
    # Because they are in ascending order, the moment the current item is different than the previous we can replace the one before it. Leetcode uses the count you provide when looping through the original array
    c = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[c] = nums[i]
            c += 1
    return c