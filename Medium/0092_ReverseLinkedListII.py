def reverseBetween(self, head, left, right):
    # If they match, nothing needs to be changed
    if left == right: return head

    # Reverse from head using number of steps
    def reverse(head, steps):
        prev, curr, count = None, head, 0
        while count < steps:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
            count += 1

    # Obtain the node before the left node and the right node
    left_node_prev, left_node, right_node = None, None, None
    curr = head
    for index in range(1, right + 1):
        if index == left - 1:
            left_node_prev = curr
        if index == left:
            left_node = curr
        if index == right:
            right_node = curr
            break
        curr = curr.next
    # Save the right nodes next value to be used later
    next_right = right_node.next
    # Reverse the linkedlist starting at the left node, going the number of steps needed
    # [1, 2, 3 , 4, 5] becomes [4,3,2], we have to redirect tail.next (2) to next_right (5) [4,3,2,5]
    reverse(left_node, right - left + 1)
    left_node.next = next_right

    # If prev_left exists, connect it to the right_node, in this case thats 4; [1,4,3,2,5]
    if left_node_prev:
        left_node_prev.next = right_node
        return head
    else:
        return right_node
