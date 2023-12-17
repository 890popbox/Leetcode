def findTilt(self, root):
    total = []

    # Visit the nodes until we reach one that is nothing
    def dfs(root):
        if root is None:
            return 0
        # Visit left and right if it exists, return the sum of each side and current value
        left = dfs(root.left)
        right = dfs(root.right)
        # Store each tilt in a list to sum up later
        total.append(abs(left - right))
        return left + right + root.val

    dfs(root)
    return sum(total)
