class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(root, word):
            cur = root
            for index, c in enumerate(word):
                if c == '.':
                    for child in cur.children.values():
                        if dfs(child, word[index + 1:]):
                            return True
                    return False
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.endOfWord

        return dfs(self.root, word)
        
