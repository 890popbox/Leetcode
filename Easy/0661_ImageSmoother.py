def imageSmoother(self, img):
    row, col = len(img), len(img[0])

    # Return the average of the position we are viewing and its surrounding squares
    def average(r, c):
        count, avg = 1, img[r][c]
        # Check the row above
        if r - 1 >= 0:
            avg += img[r - 1][c]
            count += 1
            if c - 1 >= 0:
                avg += img[r - 1][c - 1]
                count += 1
            if c + 1 < col:
                avg += img[r - 1][c + 1]
                count += 1
        # Check the row below
        if r + 1 < row:
            avg += img[r + 1][c]
            count += 1
            if c - 1 >= 0:
                avg += img[r + 1][c - 1]
                count += 1
            if c + 1 < col:
                avg += img[r + 1][c + 1]
                count += 1
        # Check the current row
        if c - 1 >= 0:
            avg += img[r][c - 1]
            count += 1
        if c + 1 < col:
            avg += img[r][c + 1]
            count += 1
        return avg // count

    # Return a new r*c list, using the average of the position we are viewing
    return [[average(r, c) for c in range(0, col)] for r in range(0, row)]
