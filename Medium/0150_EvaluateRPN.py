def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    # Scan each token, push numbers into stack and perform operators
    # If we are dealing with an operator and the stack has at least 2 items
    # This would need to be checked in other cases but not leetcode setup
    for t in tokens:
        # It's important the way division and subtraction faces
        if t == '+':
            stack.append(stack.pop() + stack.pop())
        elif t == '-':
            x, y = stack.pop(), stack.pop()
            stack.append(y - x)
        elif t == '*':
            stack.append(stack.pop() * stack.pop())
        elif t == '/':
            x, y = stack.pop(), stack.pop()
            stack.append(int(y / x))
        else:
            stack.append(int(t))
    return stack[-1]

# This leetcode evaluates correctly on Python3 and above, int division may round -0.05 to -1 in Python
