def hIndex(self, citations):
    # Descending order sort, to count each paper at h-index that has at least that many citations
    # Increase h until this condition fails and return h
    citations.sort(reverse=True)
    h = 0
    while h < len(citations) and citations[h] > h:
        h += 1
    return h
