def addTwoNumbers(self, l1, l2):
    # Create two variables to hold the value from both lists
    val1, val2 = 0, 0

    # Fill the first stack with elements from list 1
    while l1:
        val1 = val1 * 10 + l1.val
        l1 = l1.next

    # Fill the second stack with elements from list 2
    while l2:
        val2 = val2 * 10 + l2.val
        l2 = l2.next

    # Create the list node, result will be the pointer while head keeps track of the start
    head = ListNode()
    result = head

    # Fill to ListNode with the result
    for c in str(val1 + val2):
        result.next = ListNode(c)
        result = result.next

    # Return the head.next because head is default zero, the rest is added on
    return head.next
