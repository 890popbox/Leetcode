def leafSimilar(self, root1, root2):
    # Depth search, if root is None
    def dfs(root, output):
        if root is None:
            return
        if root.left is None and root.right is None:
            output.append(root.val)
        dfs(root.left, output)
        dfs(root.right, output)

    # Create two lists to hold our result for both trees, run DFS on both trees, passing through the list to fill
    output1, output2 = [], []
    dfs(root1, output1)
    dfs(root2, output2)
    # Check if these two lists are equal to each other
    return output1 == output2
