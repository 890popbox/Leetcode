def findSecondMinimumValue(self, root):
    '''
    self.smallest, self.second = root.val, sys.maxint
    # Create a function to preorder search the tree
    def pre(root):
        # If this root still exists check if that value is greater than the smallest value
        # and less than the current second lowest value, if so, update the second minimum
        # These are all non-inclusive, this will operation will not happen if they are the same
        if root:
            if self.smallest < root.val < self.second:
                self.second = root.val
            pre(root.left)
            pre(root.right)
    # Recursive way to scan the tree, return second if it is less than sys max otherwise the numbers are equal
    '''
    val = sys.maxint
    stack = [root]
    while stack:
        node = stack.pop()
        # If this nodes value is different than the roots value
        if node.val != root.val:
            val = min(val, node.val)
        # If one leaf exists, both do, add them to the stack
        if node.left:
            stack.append(node.left)
            stack.append(node.right)
    return val if val<sys.maxint else -1
# Recurs and Iteratives solutions to scan a Tree and update its second minimum
