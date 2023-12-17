def addTwoNumbers(self, l1, l2):
    # The list, head to keep track, and a carryFlag
    l3 = ListNode()
    head = l3
    carry = 0
    # While one of the linkedlists holds true
    while l1 or l2:
        # Init both values to zero
        x = y = 0

        # Move to the next nodes if available, and count their value
        if l1:
            x = l1.val
            l1 = l1.next
        if l2:
            y = l2.val
            l2 = l2.next

        # Count up the total, including carry, first time its blank, next could be
        total = carry + x + y
        carry = total // 10

        # Pass the value to the next Node
        l3.next = ListNode(total % 10)
        l3 = l3.next

    # If the carryFlag exists still, add it
    if carry:
        l3.next = ListNode(carry)
    return head.next

# Init setting both values to zero, two operations can preform if that node exists rather than seperately
# Including the carry in or won't compare until both lists are empty, but it will run through a few operations before adding the Node. We already have the carry so we can add it after.
