def minOperations(nums, k):
    # Create an array to fill with numbers
    output, array = 0, []
    # Run this loop until we fill the array enough
    while len(array) < k:
        # Pop the least element from the array
        val = nums.pop()
        # If the value is less than or equal to k we can add it to our filler array
        if val <= k and val not in array:
            array.append(val)
        output += 1
    return output

# Going to update this to a more efficient solution
