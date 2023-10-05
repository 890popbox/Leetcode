def longestCommonPrefix(strs):
    pre = ""
    shortest = len(strs[0])

    # Find the shortest word
    for word in strs:
        if len(word) < shortest:
            shortest = len(word)

    # Check if other words have that prefix
    for i in range(0, shortest):
        for j in range(len(strs) - 1):
            if strs[j][i] != strs[j + 1][i]:
                return pre
        pre += strs[0][i]
    # Has an out if all words are the same, spoiler the function will exit much earlier on
    return pre
