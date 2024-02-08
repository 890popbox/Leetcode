def uniqueOccurrences(self, arr):
    freq = {}
    # count the freq of how much a number occurs
    for num in arr:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    # if the amount of unique numbers is equal to the the amount of unique values
    return len(freq) == len(set(freq.values()))
