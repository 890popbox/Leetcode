def findLHS(self, nums):
    # Create a dictionary to count the freq of how many times a number appears
    freq = {}
    for n in nums:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1
    # Scan the numbers and if there exists a number one greater, add their freq and record max
    length = 0
    for n in freq:
        if n + 1 in freq:
            length = max(length, freq[n] + freq[n + 1])
    return length
# This works because eventually a number will be one greater or lower, , we only need to check for one of these not both
