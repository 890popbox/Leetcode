def findMaxAverage(self, nums, k):
    # The sum of k numbers in the array, keep a total and max, the total needs to be modified
    total = sum(nums[:k])
    max_sum = total
    # Linear scan moving up once each time, keep the highest max, return the average after scan
    for i in range(0, len(nums) - k):
        total = total - nums[i] + nums[i + k]
        max_sum = max(max_sum, total)
    return float(max_sum) / k
