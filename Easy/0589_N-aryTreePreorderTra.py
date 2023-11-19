def preorder(root):
    # Check if root empty
    if root is None:
        return []
    # Create a stack to solve problem
    stack = [root]
    output = []

    # Until the stack is empty
    while stack:
        # Pop the last element from the stack
        tmp = stack.pop()

        # Append the value to output
        output.append(tmp.val)

        # Extend adds a list to a stack, [::-1] Will reverse the list of the stack
        # We are adding a reverse list so the first child is what pops off the next time around
        stack.extend(tmp.children[::-1])

    return output
