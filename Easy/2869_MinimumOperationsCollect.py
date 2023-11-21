def minOperations(nums, k):
    # Create a variable to count
    count = 0
    # Run a for loop backwards to look at each element in the array of nums
    for i in range(len(nums) - 1, -1, -1):
        val = abs(nums[i]) - 1
        # Check if the value of the index we are at is less than k or equal to it
        # Also check if the offset has been marked or not, if it has then this number has been used before
        if val < k and nums[val] > 0:
            count += 1
            nums[val] *= -1
            if count == k:
                return len(nums) - i
    # The count will be found by the time we go through N numbers
    # O(N) Time and O(1) Space
