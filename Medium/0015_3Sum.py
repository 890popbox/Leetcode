def threeSum(self, nums):
    output = []
    nums.sort()
    last_index = len(nums) - 1
    # Sort the numbers then look through each one starting from index 0
    for x in range(0, len(nums)):
        target = nums[x]
        # If our first number is greater than zero, nothing in array will work
        if target > 0:
            break
        # If the last number was the same, continue to get distinct numbers
        if x > 0 and target == nums[x - 1]:
            continue
        y, z = x + 1, last_index
        target *= -1
        # while we haven't hit the last_index
        while y < z:
            # use nums[x] as the base target to hit, the sum of y/z must hit this to be valid
            sum2 = nums[y] + nums[z]
            # array is sorted so move until sum2==target otherwise y will just pass z
            if sum2 < target:
                y += 1
            elif sum2 > target:
                z -= 1
            else:
                output.append([-target, nums[y], nums[z]])
                y += 1
                z -= 1
                # append and then move them we want distinct items
                while y < z and nums[y] == nums[y - 1]:
                    y += 1
    return output
