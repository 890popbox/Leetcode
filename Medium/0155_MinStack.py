class MinStack(object):

    def __init__(self):
        # keep track of smallest value in stack, stack is a list
        self.minimum = []
        self.stack = []

    def push(self, val):
        # update the minimum if need and append, O(1)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self):
        # removing last item in the list, O(1)
        if self.stack[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.stack.pop()

    def top(self):
        # returning any item is O(1)
        return self.stack[-1]

    def getMin(self):
        # return the smallest value we saved in this object as a var O(1)
        return self.minimum[-1]
