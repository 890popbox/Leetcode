def productExceptSelf(self, nums):
    left = nums[0]
    products = [1] * len(nums)
    # Scan through the array and create a new array where the index is the product of numbers left to right
    for i in range(1, len(nums)):
        products[i] *= left
        left *= nums[i]
    # The product of the results left to right and right to left will be the final answer
    # We can do this in place by updating a variable with that information
    right = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        products[i] *= right
        right *= nums[i]
    return products
# We want to update right value in such a way that it's the product of multiplying right to left
# While using it to update the product[i] that we are viewing
