class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        # Direction of neighbor
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        res = []
        
        
        pacific = set()
        atlantic = set()

        # Cell that can reach pacific ocean
        def dfsPacific(r, c, start):
            if (r,c) in pacific:
                return

            if start:
                for x in range(ROWS):
                    dfsPacific(x, 0, False)
                for y in range(COLS):
                    dfsPacific(0,y, False)
            else:
                pacific.add((r,c))
                for dx, dy in directions:
                    newX = r + dx
                    newY = c + dy
                    if newX < 0 or newX >= ROWS or newY < 0 or newY >= COLS:
                        continue

                    if heights[newX][newY] >= heights[r][c]:
                        dfsPacific(newX, newY, False)

        # Cell that can reach atlantic ocean
        def dfsAtlantic(r, c, start):
            if (r,c) in atlantic:
                return

            if start:
                for x in range(ROWS):
                    dfsAtlantic(x, COLS - 1, False)
                for y in range(COLS):
                    dfsAtlantic(ROWS - 1,y, False)
            else:
                atlantic.add((r,c))
                for dx, dy in directions:
                    newX = r + dx
                    newY = c + dy

                    if newX < 0 or newX >= ROWS or newY < 0 or newY >= COLS:
                        continue

                    if heights[newX][newY] >= heights[r][c]:
                        dfsAtlantic(newX, newY, False)

        dfsPacific(-1,-1,True)
        dfsAtlantic(-1,-1,True)
        res = pacific.intersection(atlantic)
        return [[r,c] for r,c in res]
           