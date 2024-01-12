def rotate(self, matrix):
    # STEP ONE: Transpose matrix, diagonal swap, example: position 1,3 swaps with 3,1
    # 0,0, 1,1, etc are not effected, so lets move up every swap to avoid redundent comparisons
    n = len(matrix)
    for r in range(0, n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # STEP TWO: Reverse each row in place
    for r in range(0, n):
        matrix[r].reverse()

    # two in-place operations are required to rotate by 90*
    # transposing matrix by diagonally swapping items
    # if transposing is done first reverse each row
    # if transposing is done second reverse the matrix as if it were a palindrome
