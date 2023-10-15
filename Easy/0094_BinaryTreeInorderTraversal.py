def inorderTraversal(root):
    # If the root is empty, return it
    if root is None:
        return root
    # One array for the q, the other we must return excluding None
    q = [root]
    ls = []
    # Go until the q is empty, add the left and right each time
    # This is an altered version of pre-order traversal, If the root exists we will append it
    # to the q and then go left, what this means is the farthest item to the left will be added before others
    while q:
        # If the root exists, add the left side to q and keep going left
        if root:
            q.append(root)
            root = root.left
        # If the root no longer exists, we can't keep going left
        # Pop off the last thing we added and append its value
        # (This will be the farthest left, then rights will be considered)
        else:
            root = q.pop()
            ls.append(root.val)
            root = root.right
    # Finally before returning the array we pop the final element because root is used twice
    # Once to prime the beginning of the loop, and again to finally empty the array, this is constant time.
    ls.pop()
    return ls
