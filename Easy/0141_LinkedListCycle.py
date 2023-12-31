def hasCycle(self, head):
    fast = head
    while fast and fast.next:
        head = head.next
        fast = fast.next.next
        if head == fast:
            return True
    return False
# tortoise and hare, slow/fast cycle they eventually always catch up to each other after hare does first lap
