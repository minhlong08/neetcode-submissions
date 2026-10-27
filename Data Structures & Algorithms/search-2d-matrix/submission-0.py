class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # dimensions
        m = len(matrix)
        n = len(matrix[0])

        top, bot = 0, m - 1

        # binary search to find the row first
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                # target larger than the largest value in this row
                top = row + 1
            elif target < matrix[row][0]:
                # target smaller than the smallest value in this row
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False