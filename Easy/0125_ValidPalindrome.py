def isPalindrome(self, s):
    l, r = 0, len(s) - 1
    while r > l:
        # check if we are still in bounds, and if character is alphanumeric
        while r > l and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        # check if they don't match
        if s[l].lower() != s[r].lower():
            return False
        # move pointers to the middle of string
        l += 1
        r -= 1
    return True
