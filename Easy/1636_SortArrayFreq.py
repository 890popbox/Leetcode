def frequencySort(self, nums):
    dic = {}
    # Create a dictionary to count the freq of how many times a number appears
    for n in nums:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    # Sort the original list using freq as the key, descending order within that freq
    return sorted(nums, key=lambda x: (dic[x], -x))
