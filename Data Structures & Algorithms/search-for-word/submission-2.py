class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])

        
        flag = False

        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(x, y, curString):
            nonlocal flag
            if flag: # already find the result
                return
            if visited[x][y]:
                return

            curString += board[x][y]
            if not word.startswith(curString):   # wrong letter, stop this path
                return
            if curString == word:                # check immediately
                flag = True
                return
            visited[x][y] = True

            for dx, dy in direction:
                newX = x + dx
                newY = y + dy
                if newX < 0 or newX >= rowLen or newY < 0 or newY >= colLen:
                    continue

                if not visited[newX][newY]:
                    dfs(newX, newY, curString)
            visited[x][y] = False

        for row in range(rowLen):
            for col in range(colLen):
                if flag:
                    return flag
                    
                if board[row][col] == word[0]:
                    visited = [[False] * colLen for _ in range(rowLen)]
                    dfs(row, col, '')

        return flag



        