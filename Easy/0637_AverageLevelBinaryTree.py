def averageOfLevels(self, root):
    output = []
    q = deque([root])
    while q:
        # keep track of the summ and go until count is over
        count = len(q)
        summ = 0
        for i in range(0, count):
            ptr = q.popleft()
            summ += ptr.val
            # add each side if they exist
            if ptr.left:
                q.append(ptr.left)
            if ptr.right:
                q.append(ptr.right)
        output.append(float(summ) / count)
    return output
