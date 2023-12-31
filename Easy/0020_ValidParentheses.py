def isValid(self, s):
    # map right parathesis to left for faster access
    mapp = {")": "(", "]": "[", "}": "{"}
    # If the length is odd or we start with a right parathesis, must be False
    if len(s) % 2 != 0 or s[0] in mapp:
        return False
    # (, {, [  ... ), }, ]
    ls = []
    for c in s:
        # If the character is an opening bracket
        if c in '({[':
            ls.append(c)
        # If the character is a closing bracket
        else:
            # If list is empty too early, or the character does not match what it should
            if not ls or (ls[-1] != mapp[c]):
                return False
            ls.pop()
    # If the list is not 0, it will be false
    return not ls
