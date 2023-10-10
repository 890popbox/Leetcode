def removeElement(nums, val):
    # This is just like the removing duplicates problem except we provided with a specific number to look for and
    # remove, we do this here by simply not accepting that number to the array. Leetcode uses the count you provide
    # when looping through the original array
    c = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[c] = nums[i]
            c += 1
    return c