def reverseVowels(self, s):
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

    s = list(s)
    l, r = 0, len(s) - 1

    while l < r:
        # sliding window to the vowels and stay in range
        while l < r and s[l] not in vowels:
            l += 1
        while l < r and s[r] not in vowels:
            r -= 1
        # swap and move both pointers, if we hit the end it's just swapping the same spot
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)
