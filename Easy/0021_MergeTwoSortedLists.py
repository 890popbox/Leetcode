# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # Create the head and pointer of the Node
    head = ListNode()
    ptr = head
    # While they are both not None
    while list1 and list2:
        # If list1 val is less than or equal to list2 add it
        if list1.val <= list2.val:
            ptr.next = ListNode(list1.val)
            list1 = list1.next
        # Otherwise two is less than for sure, doesn't matter where the equal is added
        else:
            ptr.next = ListNode(list2.val)
            list2 = list2.next
        ptr = ptr.next

    # Add whichever one that didn't hit None first, all of the remaining LinkedList
    if list1:
        ptr.next = list1
    else:
        ptr.next = list2

    return head.next
