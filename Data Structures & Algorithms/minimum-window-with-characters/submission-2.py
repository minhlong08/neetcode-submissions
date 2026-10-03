class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ""

        # Count the frequency of letter in s (later) and t
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c,0) + 1

        # Keep track if the condition has been met
        have = 0
        need = len(countT)

        # Keep track of result
        index = [-1, -1]
        minLen = float("inf")
        # left index initialise to 0
        l = 0

        for r in range(len(s)):
            if s[r] not in countT:
                continue
            
            # Update the frequency of the window
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] == countT[s[r]]:
                have += 1

           
            while have == need:
                # Update the result
                if (r - l + 1) < minLen:
                    minLen = (r - l + 1)
                    index = [l, r]

                # while the condition is met, try to reduce the window size
                if s[l] in countT:
                    window[s[l]] -= 1

                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l = l + 1

        l, r = index
        return s[l:r+1] if minLen != float("inf") else ""
        


            

