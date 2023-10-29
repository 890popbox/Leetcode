def isBalanced(root):
    # If the root is Empty, it is balanced
    if root is None:
        return 1
    # Check the left and right side of the Tree
    left = isBalanced(root.left)
    right = isBalanced(root.right)
    # If either side is false or the height is over 1, the Tree isn't balanced
    if left == False or right == False or abs(left - right) > 1:
        return False
    return max(left, right) + 1
