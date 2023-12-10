def removeDuplicates(self, s):
    # Create a stack to keep track of items, and go through each character in the string
    stack = []
    for c in s:
        # If the stack exists and the last item is equal to the current, pop it off and don't append
        # If the last item in stack is not equal to current, append to stack and move on
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)
