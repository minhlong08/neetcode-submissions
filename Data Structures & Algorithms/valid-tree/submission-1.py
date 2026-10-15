class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # parents list keep track of which component a node belongs to
        # parents[2] = 1 -> node 2 belong to same component where node 1 is the root
        parents = [-1]*n
        ranks = [-1]*n
        for i in range(n):
            # initialise for each node to be its own component
            parents[i] = i
            ranks[i] = 0
        
        def find(x):
            if parents[x] != x:
                # path compression
                parents[x] = find(parents[x])

            return parents[x]
        
        
        for e in edges:
            u, v = e

            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                # 2 endpoint of the edge already in the same components -> a cycle
                return False
            
            # efficient merging: merge the smaller tree into bigger one
            if ranks[u] < ranks[v]:
                parents[rootU] = rootV
            elif ranks[u] > ranks[v]:
                parents[rootV] = rootU
            else:
                parents[rootU] = rootV
                ranks[rootV] += 1


        for ind in range(1,n):
            if find(ind) != find(ind - 1):
                return False
        # no cycle detected and every node in the same component -> valid graph
        return True 