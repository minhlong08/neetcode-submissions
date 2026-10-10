class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r,c,i): # row index, col index, current letter finding in word
            if i == len(word):
                return True # found the word

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or board[r][c] != word[i] or (r,c) in path):
                return False

            # Explore this current cell neighbor
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row,col,0):
                    return True

        return False