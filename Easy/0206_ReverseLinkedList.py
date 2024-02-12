def reverseList(self, head):
    prev, curr = None, head
    while curr != None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
