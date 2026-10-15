class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list and use dfs
        adj = {}
        for i in range(n):
            adj[i] = []

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(x):
            if x in visited:
                return
            
            visited.add(x)
            for nei in adj[x]:
                dfs(nei)

        count = 0
        for vertex in range(n):
            if vertex not in visited:
                count += 1
                dfs(vertex)

        return count
