def searchBST(self, root, val):
    # This tree is binary, let's search in the direction we need to using a smart simple dfs approach
    # We will either find the answer and return it or return None because it has not been found
    def dfs(root):
        if root == None: return None
        if root.val == val: return root
        if root.val > val:
            return dfs(root.left)
        else:
            return dfs(root.right)

    return dfs(root)
