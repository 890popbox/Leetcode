def rotateRight(self, head, k):
    # Base check, only rotate if we need to
    if k == 0 or head is None:
        return head

    length = 1
    tail = head

    # Scan the list linear to obtain the length and tail, O(N)
    while tail.next:
        length += 1
        tail = tail.next

    # This way we don't end up going over the length required, check if we still need to rotate
    k = k % length
    if k == 0:
        return head

    length = length - k - 1
    curr = head

    # Scan the linkedlist again until we reach the item before the new head, O(N)
    while length > 0:
        curr = curr.next
        length -= 1

    # The tail points to old head, current becomes head and the node before it gets sliced making it the new tail
    root = curr.next
    curr.next = None
    tail.next = head
    return root
