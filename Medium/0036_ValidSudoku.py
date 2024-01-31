def isValidSudoku(self, board):
    # Create a list of sets for the three types of ways the puzzle can be setup
    # Nine init columns are needed, square 3x3 check each iter isn't worth, and rows can simply be added as needed
    rows = [set()]
    cols = [set() for c in range(9)]
    squares = [set() for c in range(9)]

    # O(N^2), Scan all numbers in the matrix, and add them to the appropriate set
    for r in range(9):
        for c in range(9):
            # Store the number at row,col index, we will reference this number multiple times
            num = board[r][c]
            if num == '.':
                continue
            # If this number exists in the same row, column or square it is not valid
            if num in rows[r] or num in cols[c]:
                return False
            # The numbers square is the formula below, k==0 represents the first square
            # The last square k==8, range(0,9) highest row,col index is 8
            k = (r // 3) * 3 + c // 3
            if num in squares[k]:
                return False
            # Otherwise, add this number to it's respective row, column, and square
            rows[r].add(num)
            cols[c].add(num)
            squares[k].add(num)
        # Every time we finish checking a column, we move onto the next row
        rows.append(set())
    return True
