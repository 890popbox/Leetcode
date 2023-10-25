def longestPalindrome(s):
    # Base check, if the solution is one or empty, must be that string, otherwise check
    if len(s) <= 1:
        return s

    # Function to help expand, and return the moment the string is not a Palindrome
    def expandPalindrome(l, r):
        # While the pointers haven't past each other
        size = len(s)
        while l >= 0 and r < size:
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        return s[l + 1:r]

    # Save the output
    output = ""
    # Scan through the string and get substrings
    for a in range(len(s)):
        # Create two substrings where the center is offset by one
        sub1 = expandPalindrome(a, a)
        sub2 = expandPalindrome(a, a + 1)
        # Save result as the max, then update the max
        result = max(sub1, sub2, key=len)
        output = max(output, result, key=len)
    # Return the output, this will be the longest substring that is still a Palindrome
    return output


# To do this in O(N) time research Manacher's Algorithm


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("ac"))
