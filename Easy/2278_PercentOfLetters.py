def percentageLetter(self, s, letter):
    count = 0
    for c in s:
        if c == letter:
            count+=1
    return count*100//len(s)
# Store one variable to count, only count if letter is equal to, scan O(N)
# Return int of the division, no need for more variables
