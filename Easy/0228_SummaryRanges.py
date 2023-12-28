def summaryRanges(self, nums):
    output = []
    start = 0
    i = 0
    # build a range from start to end until the next number is not one greater
    while i < len(nums):
        start = nums[i]
        # keep moving forward until we are out of bounds or the next number isn't one greater
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
        # add this range to the output as a formatted string, if start==end numbers are same
        if start != nums[i]:
            output.append('{0}->{1}'.format(start, nums[i]))
        else:
            output.append('{0}'.format(start))
        i += 1
    return output
