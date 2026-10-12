class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])

        # add word to the Trie
        trie = Trie()
        for w in words:
            trie.addWord(w)

        res, visited = set(), set()
        def dfs(r, c, node, word):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r,c) in visited or 
                board[r][c] not in node.children):
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)

            # visiting neighbors
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie.root,"")

        return list(res)
