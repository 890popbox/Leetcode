from collections import deque


def maxDepth(root):
    # If root does not exist
    if root is None:
        return 0
    # Otherwise scan, keep track of the current Depth, and keep a proper queue
    depth = 0
    q = deque()
    q.append(root)
    # While the queue is not empty, run the inside, this will go until all nulls are reached
    while q:
        depth += 1
        count = len(q)  # How many items are on this level
        while count > 0:
            p = q.popleft()
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
            count -= 1
    return depth
