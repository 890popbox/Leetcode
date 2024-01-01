def maxLengthBetweenEqualCharacters(self, s):
    d = {}
    output = -1
    # mark the first time that character appears and store it in a dictionary, then compare it as it returns
    for i in range(0, len(s)):
        if s[i] in d:
            output = max(output, i - d[s[i]] - 1)
        else:
            d[s[i]] = i
    return output
