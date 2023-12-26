def isIsomorphic(self, s, t):
    # create a dictionary to map key::value pairs, and a set of values so that value only appears once
    mapp = {}
    values = set()
    # both strings are the same length, so we can check them both at once
    for c in range(0, len(s)):
        # store each strings character in a variable, key::value
        key, value = s[c], t[c]
        # if the key exists, make sure the value is the same as previous
        if key in mapp:
            if mapp[key] != value:
                return False
        mapp[key] = value
        values.add(value)
    # one to one but not one to many, dictionary and set data structures hold the length of these
    # now we have to make sure the key only maps to one value and not many
    if len(values) != len(mapp.values()):
        return False
    return True
