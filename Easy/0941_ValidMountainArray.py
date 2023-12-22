def validMountainArray(self, arr):
    # Mountain can't be smaller than 3, and the next must be greater
    if len(arr) < 3 or arr[1] <= arr[0]:
        return False
    # Scan from the start to middle, and the end to middle, both ways
    i, j = 0, len(arr) - 1
    while i < j and arr[i + 1] > arr[i]:
        i += 1
    if i == 0: return False
    while j > 0 and arr[j - 1] > arr[j]:
        j -= 1
    # Make sure they both equal each other and the start/end have moved
    return i == j and j != len(arr) - 1
