def lengthOfLongestSubstring(s):
    # Creating items for storage
    chrSet = set()
    count, i = 0, 0
    # scan the whole string O(N)
    for c in range(len(s)):
        # If the character ever appears in the dict
        while s[c] in chrSet:
            chrSet.remove(s[i])  # Set is smaller than dictionary and easier to do lookups
            i += 1
        chrSet.add(s[c])
        count = max(count, c - i + 1)

    # in order to get an array of substrings this would be created in the loop
    # count variable will return the biggest substring size
    return count