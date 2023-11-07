def countNodes(root):
    # Recursive solution
    '''
    if root is None:
        return 0
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    '''
    # Make sure the root is valid
    if root is None:
        return 0
    # Simple iterative solution, O(N), where N is each item in the Tree
    count, q = 0, [root]
    while q:
        # Pop off last element, increase the count O(1)
        p = q.pop()
        count += 1
        # Check both sides to make sure this node exists
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)
    return count