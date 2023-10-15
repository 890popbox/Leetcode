def isSameTree(self, p, q):
    # Let's try this iteratively, we will use a stack to achieve this
    s = [p, q]
    while s:
        # Pop off the first tree, then the second
        p, q = s.pop(), s.pop()

        # If both exist, add it to the stack
        if p and q:
            # If the values don't match, tree if not the same
            if p.val != q.val:
                return False
            # Push the correct sides in properly if they exist or not
            s.append(p.left)
            s.append(q.left)
            s.append(p.right)
            s.append(q.right)
        # If one exists but the other doesn't, tree is not the same
        elif p or q:
            return False
        # By checking these the last thing to consider is if both are None, which would be True, keep scanning Tree
    # The while loop handles 3 cases and if it never returns False, both Trees must be the same
    return True