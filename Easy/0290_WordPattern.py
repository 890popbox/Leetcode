def wordPattern(self, pattern, s):
    # pattern must have as much characters as words
    words = s.split(' ')
    if len(pattern) != len(words):
        return False
    # key::values stored in a map, using a set of values to ensure match
    mapp = {}
    values = set()
    for key, value in zip(pattern, words):
        # if the key is not mapped but the value is already, return false otherwise map the value
        if key not in mapp:
            if value in values:
                return False
            mapp[key] = value
            values.add(value)
        # if the key is mapped but it doesn't match the value, return false
        elif key in mapp and mapp[key] != value:
            return False
    return True
