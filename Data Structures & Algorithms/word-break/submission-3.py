class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up approach
        # dp[i] = true if s[i:] can be segmented

        dp = [False] * (len(s) + 1)
        # base case: empty string can always be segmented
        dp[len(s)] = True

        for i in range(len(s) - 1,-1,-1):
            for w in wordDict:
                # if at index i, s[i:] start with w
                # and our dp programming has calculated that s[i + len(w):]
                # can also be segmented (dp[i + len(w)] == True)
                # then s[i:] can be segmented too
                if s.startswith(w, i) and dp[i + len(w)]:
                    dp[i] = True
                    break;
        return dp[0]