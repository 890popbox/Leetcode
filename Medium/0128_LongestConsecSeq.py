    def longestConsecutive(self, nums):
        if not nums:
            return 0
        # Sorting method O(N log N) and constant space, must return zero early if empty
        nums.sort()
        currLen , maxLen = 1, 1
        # If array has numbers then the min lcs is 1, that will be our start on both variables
        for i in range(1, len(nums)):
            # If the number is the same ignore it and go next, do not remove or create progress
            if nums[i-1]==nums[i]:
                continue
            # When a number is out of sync, update max length and reset the current count
            # This is faster than updating every single number, return this to account for the final number
            if nums[i-1]+1!=nums[i]:
                maxLen = max(maxLen, currLen)
                currLen=0
            currLen+=1
        return max(maxLen, currLen)

# Hashmap/Set approach below, O(N) time and space for the size of the hashmap/set
# In theory this approach can be reversed to end rather than start

'''
# Create the hashmap, and store a value that will be the max longest consec seq
s = set(nums)
res = 0
for num in nums:
    # Scan all numbers until we find the start of the seq, the start of the seq will not have a number before it
    if num-1 not in s:
        length = 0
        # Now simply count the length of this sequence and compare it to the current max
        while num+length in s:
            length += 1
        res = max(res, length)
return res
'''
