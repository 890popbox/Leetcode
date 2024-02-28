def isPalindrome(self, head):
    rev = None
    slow = fast = head
    # Store half the list in Rev
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    # If we haven't hit None yet, move slow up to the end
    if fast:
        slow = slow.next

    # Compare the values; Rev middle to beginning, Slow is middle to end
    while slow:
        if slow.val != rev.val:
            return False
        else:
            slow, rev = slow.next, rev.next

    return True
