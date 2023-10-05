def isValid(s):
    # If the length is odd, it must be false
    if len(s) % 2 != 0:
        return False
    # (, {, [  ... ), }, ]
    ls = []
    for c in s:
        # If the character is an opening bracket
        if c in '({[':
            ls.append(c)
        # If the character is a closing bracket
        else:
            # You could probably do all this with a dictionary but its more space
            if not ls or (c == ')' and ls[-1] != '(') or (c == '}' and ls[-1] != '{') or (c == ']' and ls[-1] != '['):
                return False
            ls.pop()
    # If the list is not 0, It will be false
    return not ls
