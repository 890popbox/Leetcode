def mergeKLists(self, lists):
    # check our edge cases
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = self.mergeKLists(lists[:mid])
    right = self.mergeKLists(lists[mid:])

    return self.merge(left, right)


# helper method to merge two linkedlists into ascending order
def merge(self, l1, l2):
    dummyNode = ListNode(0)
    curr = dummyNode
    # go until one has no elements
    while l1 and l2:
        # append to the dummyList in ascending order
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    # whichever still has elements
    curr.next = l1 or l2
    return dummyNode.next
