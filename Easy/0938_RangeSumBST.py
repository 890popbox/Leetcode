def rangeSumBST(self, root, low, high):
    # If the root does not exist
    if root is None:
        return 0
    # Create a variable to hold the result, and a queue to traverse, run until empty
    output = 0
    q = [root]
    while q:
        p = q.pop()
        # If the value falls between the range, add it to the output
        if low <= p.val <= high:
            output += p.val
            # Add these nodes to the queue if they exist
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        # If the value does not fall between the range decide which way to add a node
        # If the value is lower, add the right, else would be if the value is higher
        # If the value isn't lower or in between the range it must be higher, no need to compare
        # Append if it exists, we don't have to check both sides
        elif p.val < low:
            if p.right is not None:
                q.append(p.right)
        else:
            if p.left is not None:
                q.append(p.left)
    return output
