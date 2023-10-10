# Creating a Queue in Python using a list, could also use a LinkedList
"""
A Queue is just a Data Structure meant to act as a line. First in first out (FIFO)
These would probably be made with a LinkedList as you don't expect to use as much functionality and memory as a list
"""


class Queue1(object):
    # Keep track of the size and list
    def __init__(self):
        self.size = 0
        self.list = []

    def enqueue(self, val):
        self.list.append(val)
        self.size += 1

    def dequeue(self):
        # Only do it if there are items in the list
        if self.size > 0:
            self.list.pop(0)
            self.size -= 1

    def peek(self):
        return self.list[0]