class Solution(object):
    # in order traversal so numbers are stored sorted without having to sort them
    def __init__(self):
        self.values = []

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.values.append(root.val)
            self.inOrder(root.right)

    def getMinimumDifference(self, root):
        self.inOrder(root)

        # there isn't a need for edge check there will be 2 or more numbers
        min_diff = abs(self.values[0] - self.values[1])

        # now that numbers have been added and sorted in an array, find the closest distance by linear scan
        for i in range(2, len(self.values)):
            diff = abs(self.values[i - 1] - self.values[i])
            if diff < min_diff: min_diff = diff

        return min_diff
