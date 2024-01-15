def invertTree(self, root):
    if root is None:
        return root
    stack = [root]
    # go while we have valid nodes
    while stack:
        node = stack.pop()

        # swap the left and right, None is okay here
        tmp = node.left
        node.left = node.right
        node.right = tmp

        # add to the stack if exists
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root


# Recursive approach
'''
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
'''
