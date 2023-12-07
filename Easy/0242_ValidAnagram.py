def isAnagram(s, t):
    # Create a dictionary to store characters in both words
    d = {}
    # Return early if words are not the same length
    if len(s) != len(t):
        return False
    # Scan the first word, increasing the value if the character appears
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    # Scan the second word, decreasing the value if the character appears
    for c in t:
        if c not in d:
            return False
        d[c] -= 1
    # Scan the dictionary, if anything does not equal zero return false
    for v in d.values():
        if v != 0:
            return False
    return True
