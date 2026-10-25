class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i+1,n):
                # swap matrix[i][j] with matrix[j][i]
                # python quick syntax without using a temp var
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for row in matrix:
            row.reverse()

        return