def isSubsequence(self, s, t):
    j, l = 0, len(s)
    # scan the long string left to right comparing with small strings pointer
    for i in range(0, len(t)):
        # if all length has been travelled, a valid subsequence can be made
        if j == l:
            return True
        if t[i] == s[j]:
            j += 1
    return j == l
