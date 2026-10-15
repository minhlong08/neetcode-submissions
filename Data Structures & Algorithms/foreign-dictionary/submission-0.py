class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Idea: if we can infer letter 'a' < letter 'b' -> Build an edge from 'a' to 'b'
        # Valid lexicographically will be the topological order of the graph
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for w1, w2 in zip(words, words[1:]):
            for c1,c2 in zip(w1,w2):
                if c1 != c2:
                    # w1 come before w2 -> c1 must come before c2
                    # add an edge c1->c2
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
            else: # this only run if break was never hit
                if len(w1) > len(w2):
                    return ""

        q = deque(c for c in indegree if indegree[c] == 0)
        res = []

        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        # If some letters were never output, there was a cycle
        return "".join(res) if len(res) == len(adj) else ""
