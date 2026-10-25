class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = []
        top, bottom = 0, ROWS - 1
        left, right = 0, COLS - 1

        while top <= bottom and left <= right:
            # 1. left -> right along the top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # 2. top -> bottom along the right row
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # 3. right -> left along the bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            # 4. bottom -> top along the left row
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        

        return res