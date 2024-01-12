def containsNearbyDuplicate(self, nums, k):
    d = {}
    # scan list linear and store the last index that number was seen in
    for index, num in enumerate(nums):
        # if the last index fits our condition return true, no need for abs when last number should be lower
        if num in d and index - d[num] <= k:
            return True
        # update index regardless of if it exists or not
        d[num] = index
    return False
