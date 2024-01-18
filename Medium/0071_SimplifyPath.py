def simplifyPath(self, path):
    # Split the path by slash and only count existing folders
    # Only pop if possible and we are moving up
    stack = []
    for folder in path.split('/'):
        if folder == '..':
            if stack: stack.pop()
        elif folder and folder != '.':
            stack.append(folder)
    # Root plus the stack, where each folder gets a slash after
    return '/' + '/'.join(stack)
