class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = [[False] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0':
                    visited[r][c] = True

        def dfs(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or visited[r][c]):
                return
            
            visited[r][c] = True
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not visited[r][c]:
                    res += 1
                    dfs(r,c)

        return res

