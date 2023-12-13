def removeElements(self, head, val):
    # Remove node until head is no longer equal to the value
    while head is not None and head.val == val:
        head = head.next
    # If the head does not exist, return nothing
    if head is None:
        return head
    # Store a pointer keeping track of prev and current
    current = head
    # While the next item exists and is not None
    while current.next:
        # If next value needs to be removed, move the next pointer up twice
        # Otherwise move up once normally
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return head
