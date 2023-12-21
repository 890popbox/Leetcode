def findDifference(self, nums1, nums2):
    # Create two sets filled with the items from the lists
    # You could also do this with a dictionary, create a list to hold output
    set1 = set(nums1)
    set2 = set(nums2)
    # Subtracting sets takes the first set and removes items in it that are equal to the second set
    return [set1 - set2, set2 - set1]
