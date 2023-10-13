def merge(nums1, m, nums2, n):
    # I'm going to merge these in place with array 1, once everything in array 2 is moved we can stop
    # While array 2 number is greater than zero
    while n > 0:
        # Checking both these for > 0 because we are subtracting by one to get the correct position
        # So if it exists, and the number is greater that's the number we will be putting in
        if m > 0 and nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        # If its not greater its either less or equal, which the equal doesn't matter what position it is in
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        # In both cases the method only moves the pointer it needs to
