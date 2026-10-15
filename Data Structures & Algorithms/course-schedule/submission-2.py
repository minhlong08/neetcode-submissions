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
        
        # Storing the indegree (number of prerequisites) of each vertex
        indegree = [0] * numCourses
        for u in g.adj:
            for v in g.get_neighbors(u):
                indegree[v] += 1

        # possible to finish all course if there is a valid topological order of the graph
        q = deque()
        for v in g.adj:
            if indegree[v] == 0:
                q.append(v)

        # Kahn algorithm

        #keep track of the number of vertices in the topological order
        # if count == number of vertices -> exist a valid topological order
        count = 0
        while q:
            u = q.popleft()
            count += 1

            for v in g.get_neighbors(u):
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        return count == numCourses
        