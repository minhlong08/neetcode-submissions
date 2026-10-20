class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Top down approach
        memo = {}
        def dfs(index):
            if index == len(s):
                return True
            elif index in memo:
                return memo[index]

            targetStr = s[index:]
            for w in wordDict:
                if targetStr.startswith(w):
                    length = len(w)
                    if dfs(index + length):
                        memo[index] = True
                        return True
            memo[index] = False
            return False

        return dfs(0)