def countConsistentStrings(self, allowed, words):
    sett = set(allowed)
    output = len(words)
    # Scan each word in words and the characters within it
    for word in words:
        for c in word:
            if c not in sett:
                output -= 1
                break
    return output
