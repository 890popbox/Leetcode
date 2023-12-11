def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
    # We don't even have to create the matrix, we can just assume it exists, saves space
    cords = []
    # Scan each item in the matrix, this stores the cords and the distance from the given center
    for r in range(rows):
        for c in range(cols):
            cords.append([r,c])
    # We already created the list, now sort it using the distance formula
    cords.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
    return cords
# The cords size will be rows * cols, for example 3*3 = 9 items
# Then it just has to be sorted using some kind of organization method like a function.
# This is obviously a storage advantage and the larger the list is the bigger advantage to speed
