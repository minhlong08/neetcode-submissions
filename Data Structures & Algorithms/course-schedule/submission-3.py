class Graph:
    def __init__(self):
        self.adj = {}

    # add a vertex to the graph
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []
    # add an edge from u->v:
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        
        self.adj[u].append(v)

    # get neighbors of a vertex
    def get_neighbors(self, v):
        return self.adj[v]

    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # initialise a new graph g
        g = Graph()
        
        # Add every course, including isolated courses
        for v in range(numCourses):
            g.add_vertex(v)

        # prerequisite -> course
        for u, v in prerequisites:
            g.add_edge(v, u)
        
        # Using cycle detection
        # if there is a cycle -> not a DAG -> not valid order
        def hasCycle(g):
            # state = 0 -> unvisited
            # state = 1 -> visiting (on the stack)
            # state = 2 -> visited (not on the stack anymore)
            state = [0] * numCourses

            def dfs(v):
                state[v] = 1

                for u in g.get_neighbors(v):
                    if state[u] == 1:
                        return True #has cycle
                    if state[u] == 0: # not visited yet
                        if dfs(u): # found the cycle -> stop the recursion
                            return True
                state[v] = 2 #mark the vertex as finished exploring
                return False

            for v in g.adj:
                if dfs(v):
                    return True
            return False

        return not hasCycle(g)
        