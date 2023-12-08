def islandPerimeter(self, grid):
    count = 0
    # Row, col scan, O(N^2), where n is items in each row/col, or O(G) where G is items in Grid, this is constant.
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            # If we are standing on land, mark 4 sides
            if grid[r][c] == 1:
                count += 4
                # Check to the left and top if possible and only if the spot was marked
                # Right and bottom work also, in theory zero is faster to lookup and compare against
                # Remove 2 from the count, eventually we will hit this again and it would be as if we removed 1
                if r > 0 and grid[r - 1][c] == 1:
                    count -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    count -= 2
    return count
