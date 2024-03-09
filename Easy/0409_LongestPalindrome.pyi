def longestPalindrome(self, s):
    size = len(s)
    if size==1: return 1

    ss = set()
    for letter in s:
        if letter not in ss:
            ss.add(letter)
        else:
            ss.remove(letter)

    if len(ss) != 0: return size - len(ss) + 1
    return size
