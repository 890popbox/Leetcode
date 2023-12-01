def getConcatenation(nums):
    # Use and scan through the original list, append values to it until you reach its original end
    for i in range(0, len(nums)):
        nums.append(nums[i])
    # Or we can just return (nums + nums), this concates arrays in python.
    # If we can't do this just make an array and do two linear scans of the original array
    return nums