def compress(self, chars):
    curr_char = chars[0]
    count = 0
    s = []
    # Linear scan of the array, keeping track of if we find a new character
    for char in chars:
        if char == curr_char:
            count += 1
        else:
            s.append(curr_char)
            if count > 1:
                for d in str(count): s.append(d)
            curr_char = char
            count = 1

    # Append the character and if theres more than one append how many there are in single digits
    s.append(curr_char)
    if count > 1:
        for d in str(count): s.append(d)

    # Remake the array by linking pointers and return the length of characters in array
    chars[:] = s
    return len(chars)
