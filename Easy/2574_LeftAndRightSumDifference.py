def leftRightDifference(self, nums):
    # Base case, if there is only one number
    # Constraints, 1 <= nums[i] <= 10^5
    size = len(nums)
    if size == 1:
        return [0]
    # Otherwise time we write an algorithm
    # Setup a left and right list with default values at 0, and the size equal to nums
    leftSum = [0] * size
    rightSum = [0] * size
    output = [0] * size
    # Loop to sum the leftSide and move up until the end is hit
    for i in range(1, size):
        leftSum[i] += nums[i - 1] + leftSum[i - 1]
    # Loop to sum the rightSide and move up until the end is hit
    for i in range(size - 2, -1, -1):
        rightSum[i] += nums[i + 1] + rightSum[i + 1]
    # Loop to get the final result, taking the absolute value of both sides
    for i in range(0, size):
        output[i] = abs(leftSum[i] - rightSum[i])
    return output
