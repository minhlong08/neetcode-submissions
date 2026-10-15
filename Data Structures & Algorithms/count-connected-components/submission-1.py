class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Use disjoint set (union find) since we are given a list of edges
        parent = [-1] * n
        rank = [-1] * n

        for i in range(n):
            # initialise each node parent to itself
            parent[i] = i
            rank[i] = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        component = n
        for edge in edges:
            u,v = edge
            rootU = find(u)
            rootV = find(v)

            # already in the same component
            if rootU == rootV:
                continue
            
            # in seperate component -> merge and decrease component count
            component -= 1
            if rank[rootU] > rank[rootV]:
                parent[rootV] = rootU
            elif rank[rootU] < rank[rootV]:
                parent[rootU] = rootV
            else:
                parent[rootV] = rootU
                rank[rootU] += 1

        return component
                    