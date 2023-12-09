def findKDistantIndices(self, nums, key, k):
    output = []
    index = 0
    # Locate the indexes that contain the keys value
    for i in range(0, len(nums)):
        # Examine the spot where the key is found and fits the requirements
        # We can examine this key as long as (index-i <= k)
        while nums[i] == key and index - i <= k:
            # We can only add to results if absolute value works, index is increasing until we exit this loop
            # This is fast and will help us reach len(nums) quicker if multiple spots satisfy a single key
            if abs(index - i) <= k:
                output.append(index)
            index += 1
            # If the index ever reaches the size of original list
            if index == len(nums):
                return output
    return output
# There are ways to optimize the range with min/max to insure we do not loop excessively
# This is similar by only running the loop as we are able, as well as exiting the second our index reaches a length

