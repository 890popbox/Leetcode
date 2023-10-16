# This solution is the SameTree inverted
def isSymmetric(root):
    # Base case check
    if root is None:
        return True
    # Let's try this iteratively, we will use a stack to achieve this
    s = [root.left, root.right]
    while s:
        # Pop off the tree
        l, r = s.pop(), s.pop()

        # If both exist, add it to the stack
        if l and r:
            # If the values don't match, tree if not the same
            if l.val != r.val:
                return False
            # Push the correct sides in properly if they exist or not
            s.append(l.left)
            s.append(r.right)
            s.append(l.right)
            s.append(r.left)
        # If one exists but the other doesn't, tree is not the same
        elif l or r:
            return False
        # By checking these the last thing to consider is if both are None, which would be True, keep scanning Tree
    # The while loop handles 3 cases and if it never returns False, both Trees must be the same
    return True
