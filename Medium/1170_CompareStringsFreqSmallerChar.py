def numSmallerByFrequency(self, queries, words):
    # helper function to return freq of the smallest character, O(N), constant space
    # dcce == 2 because c is two
    # aabbbccccc == 2 because a is two
    def freq(word):
        char = "z"
        count = 0
        for ch in word:
            if ch < char:
                char = ch
                count = 1
            elif ch == char:
                count += 1
        return count

    # store the freq of queries and words, O(N^2) two passes
    # sort the word_freq for future use, as we scan queries
    # we will use this information to get how many words the query is less than
    query_freq = [freq(q) for q in queries]
    word_freq = [freq(w) for w in words]
    word_freq.sort()

    output = []
    n = len(word_freq)
    # binary search each of the items freq in our query to get to the result faster than brute force comparisons
    for q in query_freq:
        l, r, = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if word_freq[m] > q:
                r = m - 1
            else:
                l = m + 1
        output.append(n - l)
    return output
