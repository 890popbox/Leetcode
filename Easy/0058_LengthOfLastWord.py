def lengthOfLastWord(s):
    # return len(s.split()[-1])
    # One variable to hold the end of the string and the other to hold the length of the string
    end = len(s) - 1
    length = 0
    # First we must make sure we are on a valid character, no trailing spaces
    while end >= 0 and s[end] == ' ':
        end -= 1
    # Now that we are on a valid character we can count until we run into a space
    while end >= 0 and s[end] != ' ':
        end -= 1
        length += 1
    return length
