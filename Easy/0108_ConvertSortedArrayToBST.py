# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    # Helper function to create Tree
    def create(start, end):
        if start < end:
            mid = (start + end) // 2
            return TreeNode(nums[mid], left=create(start, mid), right=create(mid + 1, end))
        return None

    # Create the root and use start to end of array as the range
    start, end = 0, len(nums)
    # The value of the root will be the middle of the array
    return create(start, end)
