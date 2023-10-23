def addTwoNumbers(11, l2):
    # The list, head to keep track, and a carryFlag
    l3 = ListNode()
    head = l3
    carry = 0
    # While one of the linkedlists holds true
    while l1 or l2:
        # Init both values to zero
        val1, val2 = 0, 0
        # Get the correct values, if that node exists or it stays zero
        if l1:
            val1 = l1.val
            l1 = l1.next
        if l2:
            val2 = l2.val
            l2 = l2.next
        # Count up the total, including carry, first time its blank, next could be
        total = carry + val1 + val2
        digit = total % 10
        carry = total // 10
        # Pass the value to the next Node
        l3.next = ListNode(digit)
        l3 = l3.next
    # If the carryFlag exists still, add it
    if carry:
        l3.next = ListNode(carry)
    return head.next