def areAlmostEqual(s1, s2):
    # Variable to count the differences in the words, and another to mark where they occur
    c, diff = 0, -1
    for i in range(0, len(s1)):
        # If the characters are different, mark it and count
        if s1[i] != s2[i]:
            c += 1
            # If the count is ever above two, this is False
            if c > 2:
                return False
            elif diff == -1:
                diff = i
            else:
                # If the characters are different at these locations it is impossible to recreate the word
                if s1[diff] != s2[i] or s1[i] != s2[diff]:
                    return False
    # If we count zero or two differences, then one swap will satisfy
    # If we count one, three or more difference, one swap will not satisfy, it will need more or be impossible
    return False if c == 1 else True
