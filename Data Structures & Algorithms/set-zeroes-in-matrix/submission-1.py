class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowZero = False

        # 1st row of matrix keep track of which column should be 0 out
        # 1st col of matrix keep track of which row should be 0 out
        # rowZero keeo track if row 0 should be 0 out (overlapping of the 2 above so need a seperate variable to store)

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # carry out the zeroing
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # zero out the 1st row and col
        if matrix[0][0] == 0: # 1st col shoul be zero
            for i in range(ROWS):
                matrix[i][0] = 0
        
        if rowZero:
            for j in range(COLS):
                matrix[0][j] = 0

        
        return