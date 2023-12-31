def groupAnagrams(self, strs):
    # Create a dictionary and store the word sorted as a key and itself as a value
    # key == sorted word, value = original word
    d = {}
    for s in strs:
        tmp = ''.join(sorted(s))
        if tmp not in d:
            d[tmp] = []
        d[tmp].append(s)
    return d.values()
