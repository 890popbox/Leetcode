# A node that will represent the head or tail
class Node(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


# Creating a circular doubly LinkedList similar to an array
"""
The idea here is the nodes will need a next and prev, as well as the LinkedList object will need a head and tail 
to keep track. The benefit to a head and tail system make accessing the front of the data structure and end very 
quick. 
"""


class LinkedList(object):
    # Create a NULL Linked List
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = self.head

    # Adding to the Linked List
    def addNode(self, val):
        # If the head is empty create one
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
            # Have them point to each other in a circle
            self.tail.next = self.head
            self.head.prev = self.tail
        # Otherwise we are adding to the tail
        else:
            # Create a new node where it's prev points to the tail and next points to the head
            n = Node(val, self.tail, self.head)
            # The tails next should now point to this Node, then the tail pointer should be assigned to the new Node
            self.tail.next = n
            self.tail = n
            self.head.prev = self.tail
        # Increase the size of the LinkedList as this action was successful
        self.size += 1

    # Deleting from the Linked List
    def deleteNode(self, val):
        # CASE 1, Value is at head
        # CASE 2, Value is at tail
        # CASE 3, Value is inside the LinkedList
        if self.head.val == val:
            ptr = self.head
            self.head = ptr.next
            del ptr
        elif self.tail.val == val:
            ptr = self.tail
            self.tail = ptr.prev
            del ptr
        else:
            ptr = self.head
            while ptr.next.val != val and ptr.next != self.tail:
                ptr = ptr.next
            # Exit the method if it does not exist
            if ptr.next.val != val:
                return
            # Tmp is the node to delete, rearrange the pointers before deleting it
            tmp = ptr.next
            ptr.next = tmp.next
            tmp.next.prev = ptr
            del tmp
        # Update the size of the LinkedList
        self.size -= 1

    # Printing out the Linked List
    def print(self):
        ptr = self.head
        while ptr != self.tail:
            print(ptr.val)
            ptr = ptr.next
        print(ptr.val)

    # Printing out the Linked List Reversed
    def printRev(self):
        ptr = self.tail
        while ptr != self.head:
            print(ptr.val)
            ptr = ptr.prev
        print(ptr.val)


# Create the LinkedList
list1 = LinkedList()
# Add some items
list1.addNode(1)
list1.addNode(2)
list1.addNode(3)
list1.addNode(4)
list1.addNode(5)
# Let's delete Even Numbers
list1.deleteNode(2)
list1.deleteNode(4)
list1.deleteNode(6)  # Number that doesn't exist
# Print out the results forward and reversed
list1.print()
print('---')
list1.printRev()
