class Solution(object):
    path = False

    def hasPathSum(self, root, targetSum):
        if root is None:
            return
        elif root.val == targetSum and not root.left and not root.right:
            self.path = True
        if not self.path:
            self.hasPathSum(root.left, targetSum - root.val)
        if not self.path:
            self.hasPathSum(root.right, targetSum - root.val)
        return self.path


# Above implementation hopes to skip traversing the Tree once we already found a path, otherwise continue
# Simple to understand solution below, if our root.val == target return True
# Otherwise subtract the targetSum and go left or right if it exists
# Eventually the last item will be the value that makes the sum exact

'''
    if root is None:
        return False
    elif root.val == targetSum and not root.left and not root.right:
        return True
    return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
'''
