class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] number of way to decode s[:i+1]
        if not s or s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        dp = [0] * len(s)

        dp[0] = 1
        two = int(s[:2])
        if s[1] == '0':
            if two > 26:
                return 0
            dp[1] = 1
        else:
            dp[1] = 2 if 10 <= two <= 26 else 1
            
        for i in range(2,len(s)):
            two = int(s[i-1:i+1])
            if s[i] == '0':
                if not 10 <= two <= 26:
                    return 0
                # we have to merge position i with position i - 1
                # hence number of decoding is dp[i-2]
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1]
                if 10 <= two <= 26: # we can merge with position i - 1
                    dp[i] += dp[i - 2]
        
        return dp[-1]