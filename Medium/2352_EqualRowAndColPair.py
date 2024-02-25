def equalPairs(self, grid):
    # Create a dictionary that only needs to store int for the value
    d = defaultdict(int)
    for row in grid:
        d[tuple(row)] += 1
    # Compare the column and count how many times that tuple is in the dictionary
    return sum(d[tuple(col)] for col in zip(*grid))
