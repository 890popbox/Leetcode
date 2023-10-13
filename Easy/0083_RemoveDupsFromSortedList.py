# node has a val and a next pointer
def deleteDuplicates(head):
    # If there is no head, return
    if head is None:
        return head
    # Create two pointers, prev and curr, space them apart.
    prev = head
    curr = prev.next
    # While the current is not none, move ahead each time, adjust the previous based on if they are the same or not
    while curr is not None:
        if curr.val == prev.val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    # This is more for visual however we could do this with one pointer
    return head
