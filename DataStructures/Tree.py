# A node that will represent the root or a leaf

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Creating a Binary Tree Structure in Python
"""
The idea here is the nodes will need a left and right, as well as the Tree object will need a root to keep track 
of the tree's root.
"""


class Tree(object):
    # Create a NULL Tree
    def __init__(self):
        self.size = 0
        self.root = None

    # Adding to the  Tree
    def addNode(self, val):
        # If the root is empty, give it a starting point
        if self.root is None:
            self.root = Node(val)
        # Otherwise we are adding to the Tree
        else:
            # We can do this recurs or inter, recurs typically needs a helper func
            # Recurs sucks but this is probably the only time its easier than iter
            # We will go with iter anyway
            ptr = self.root
            tmp = None
            while ptr is not None:
                tmp = ptr
                # If the leaf we are on is greater than or equal the value go left
                if ptr.val >= val:
                    ptr = ptr.left
                # If the leaf we are on is less than the value go right
                elif ptr.val <= val:
                    ptr = ptr.right
            # If the leaf we are on is greater than or equal the value go left
            if tmp.val >= val:
                tmp.left = Node(val)
            # If the leaf we are on is less than the value go right
            elif tmp.val <= val:
                tmp.right = Node(val)
            self.size += 1  # Keep track of tree size

    # Deleting from the Tree
    def deleteNode(self, val):
        # If the root is empty nothing to delete
        if self.root is None:
            return

        # Start at the end and let's find the Node to delete
        ptr = self.root
        tmp = None

        # Search until we find the value
        while ptr.val != val:
            tmp = ptr  # Tmp is the Node before  the one we need to delete

            # If the leaf we are on is greater than or equal the value go left
            if ptr.val >= val:
                ptr = ptr.left
            # If the leaf we are on is less than the value go right
            elif ptr.val <= val:
                ptr = ptr.right

            # If the ptr is ever None, it doesn't exist, exit function
            if ptr is None:
                return

        # CASE 1, The node has no leafs
        if ptr.left is None and ptr.right is None:
            # If the leaf we are on is greater than or equal the value go left
            if tmp.val >= val:
                tmp.left = None
            # If the leaf we are on is less than the value go right
            elif tmp.val <= val:
                tmp.right = None

        # CASE 2, The node has a leaf on the left (And maybe the right as well)
        elif ptr.left is not None:
            # If the leaf we are on is greater than or equal the value go left
            if tmp.val >= val:
                tmp.left = ptr.left
                tmp.left.right = ptr.right
            # If the leaf we are on is less than the value go right
            elif tmp.val <= val:
                tmp.right = ptr.left
                tmp.right.right = ptr.right

        # CASE 3, The node only has a leaf on the right (This happens because of the top two cases)
        else:
            # Go right one and find the most left
            leftTmp = self.findMinNode(ptr.right)
            leftTmp.left = ptr.left
            tmp.left = leftTmp
            # If the right Node doesn't end up having any Nodes to the left of it
            leftTmp.right = None if leftTmp == ptr.right else ptr.right
        # Free up memory and keep track of size
        self.size -= 1
        del ptr, tmp

    # Find the minNode from given parent
    @staticmethod
    def findMinNode(parent):
        ptr = parent
        while ptr.left is not None:
            ptr = ptr.left
        return ptr

    # Find the maxNode from given parent
    @staticmethod
    def findMaxNode(parent):
        ptr = parent
        while ptr.right is not None:
            ptr = ptr.right
        return ptr

    # Printing out the tree
    def print(self):
        if self.root is None:
            print('Empty Tree')
        else:
            q = [self.root]
            # While the queue still has items in it
            while len(q) > 0:
                # Pop from the queue and then print it out
                ptr = q.pop(0)
                print(ptr.val)
                # Add the sides if they exist
                if ptr.left is not None:
                    q.append(ptr.left)
                if ptr.right is not None:
                    q.append(ptr.right)
        print('Size: {0} Items in the Binary Search Tree'.format(self.size))

    # Print out the min and max from the main root
    def printMinMax(self):
        head = self.root
        print(self.findMinNode(head).val)
        print(self.findMaxNode(head).val)


# Create the Tree
tree = Tree()
# Add some items
tree.addNode(8)
tree.addNode(3)
tree.addNode(10)
tree.addNode(1)
tree.addNode(6)
tree.addNode(4)
tree.addNode(7)
tree.addNode(9)
tree.addNode(14)
tree.addNode(13)
tree.addNode(15)
tree.addNode(5)
tree.addNode(2)
# Let's delete Even Numbers
tree.deleteNode(2)  # Number that doesn't exist
tree.deleteNode(4)
tree.deleteNode(3)
tree.deleteNode(10)
# Print out the results as a tree
tree.print()
print('---')
tree.printMinMax()
