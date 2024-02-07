def moveZeroes(self, nums):
    # index represents the last index of a number that is not zero
    index = 0
    # Linear scan of the array, if the number isn't zero swap
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
