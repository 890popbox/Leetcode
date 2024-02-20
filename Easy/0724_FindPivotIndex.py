    def pivotIndex(self, nums):
        left, right = 0, sum(nums)
        for i in range(0, len(nums)):
            right-=nums[i]
            if left == right:
                return i
            left+=nums[i]
        return -1
# the index we are at should be ignored, so subtract, check, then add
