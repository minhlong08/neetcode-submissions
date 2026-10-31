class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        visited = set()

        def dfs(x, y, curArea):
            nonlocal res
            # out of bound
            if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                return
            
            # already visited
            if (x,y) in visited:
                return

            # water
            if grid[x][y] == 0:
                return

            visited.add((x,y))
            curArea[0] += 1

            dfs(x + 1, y, curArea)
            dfs(x - 1, y, curArea)
            dfs(x, y + 1, curArea)
            dfs(x, y - 1, curArea)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    curArea = [0]
                    dfs(r, c, curArea)
                    res = max(res, curArea[0])
        
        return res
