def canConstruct(self, ransomNote, magazine):
    alpha = {}
    # Create a dictionary to hold if the character exists or not, and count the occurences
    for c in ransomNote:
        if c not in alpha:
            alpha[c]=0
        alpha[c]+=1
    # Scan through alpha, if the number occurences more than in magazine return false
    # Keep going until its confirmed that magazine has enough characters for the ransomNote
    for c in alpha:
        if alpha[c] > magazine.count(c):
            return False
    return True
# In theory subtracting from magazine and confirming that no character contains higher than zero may be fast
# A lot of test cases here seem to end early meaning the count is greater than the magazine, therefore no further running is needed
