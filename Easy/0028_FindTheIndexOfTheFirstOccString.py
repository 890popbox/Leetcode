def strStr(haystack, needle):
    # return haystack.find(needle)

    # Improving brute force method by starting at the beginning
    # There is a good video on longest proper suffix, but there is a lot to think about.
    # Let's create a simple solution here using the length of the needle in the haystack
    # Another way to do this is keeping an array of all the indexs that start with the first character in needle.
    # This may be fast also but will use a bit more space
    n, h = len(needle), len(haystack)

    # The haystacks length minus the needles length plus 1 is all we have to travel to
    # because we don't want to go out of bounds.
    for i in range(h - n + 1):
        # Now we start at the beginning of the needle to check for a match
        for j in range(n):
            # If it's not equal, stop the search here and continue to a start of hay that's equal to start of needle
            if needle[j] != haystack[i + j]:
                break
            # If we have gone the whole length of needle and not had to break, then it's a match
            # So if needle length minus 1 is equal to J we can return the index
            if j == n - 1:
                return i

    # If we don't find the needle in the Haystack
    return -1