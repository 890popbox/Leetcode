def isValidBST(self, root):
    def dfs(root, lower=float('-inf'), upper=float('inf')):
        # if the root doesn't exist default to True, if we are out of bounds False, continue
        if not root:
            return True
        if not (lower < root.val < upper):
            return False
        return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)

    # do a depth search keeping track of the bounds
    return dfs(root)
