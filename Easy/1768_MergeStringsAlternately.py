def mergeAlternately(word1, word2):
    # Run this loop until i is greater than the largest word
    output, i = [], 0
    while i < len(word1) or i < len(word2):
        # Check word1 then word2 if not out of bounds
        if i < len(word1):
            output.append(word1[i])
        if i < len(word2):
            output.append(word2[i])
        i += 1
    # Create a string with the characters we store, O(N)
    return ''.join(output)
