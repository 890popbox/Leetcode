def twoSum(nums, target):
    dic = {}
    for i in range(0, len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
            # [ number the index of the number that exists in the dictionary, the current index. ]
        else:
            dic[nums[i]] = i
            # current_number to save in dict = the index
