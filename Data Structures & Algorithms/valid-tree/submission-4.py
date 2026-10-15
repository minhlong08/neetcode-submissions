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
        
        components = n
        for e in edges:
            u, v = e

            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                # 2 endpoint of the edge already in the same components -> a cycle
                return False
            
            # efficient merging: merge the smaller tree into bigger one
            components -= 1
            if ranks[rootU] < ranks[rootV]:
                parents[rootU] = rootV
            elif ranks[rootU] > ranks[rootV]:
                parents[rootV] = rootU
            else:
                parents[rootU] = rootV
                ranks[rootV] += 1

        # no cycle detected and every node in the same component -> valid graph
        return components == 1