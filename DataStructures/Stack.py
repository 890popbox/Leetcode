# Creating a Stack in Python using a list, could also use a LinkedList
"""
A Stack is just a Data Structure meant to act as a line. Last in first out (LIFO)
These would probably be made with a LinkedList as you don't expect to use as much functionality and memory as a list
"""


class Stack(object):
    # Keep track of the size and list
    def __init__(self):
        self.size = 0
        self.list = []

    def push(self, val):
        self.list.append(val)
        self.size += 1

    def pop(self):
        # Only do it if there are items in the list
        if self.size > 0:
            self.list.pop()
            self.size -= 1

    def peek(self):
        return self.list[-1]