def findMedianSortedArrays(self, nums1, nums2):
    # Save the length of both arrays
    n, m = len(nums1), len(nums2)
    # Two pointers and two variables to hold the current index
    i, j = 0, 0
    o1, o2 = 0, 0
    # Find the median
    for index in range(0, (n + m) // 2 + 1):
        # Save the previous output
        o2 = o1
        # If we are still in bounds
        if i < n and j < m:
            if nums1[i] < nums2[j]:
                o1 = nums1[i]
                i += 1
            else:
                o1 = nums2[j]
                j += 1
        elif i < n:
            o1 = nums1[i]
            i += 1
        else:
            o1 = nums2[j]
            j += 1
    # Return the output based off if the condition was odd or even
    return float(o1 + o2) / 2 if ((n + m) % 2 == 0) else float(o1)
