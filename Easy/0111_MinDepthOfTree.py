def minDepth(root):
    # If the root is None
    if root is None:
        return 0
    # Keep track of two subtree depth
    l = self.minDepth(root.left)
    r = self.minDepth(root.right)
    # If both subtrees are empty
    if root.left is None and root.right is None:
        return 1
    # If the left or right subtree is empty, add one to the current value
    if root.left is None:
        return 1 + r
    if root.right is None:
        return 1 + l
    # Return the minimum value from the two subtrees and add 1 to it
    return min(l, r) + 1