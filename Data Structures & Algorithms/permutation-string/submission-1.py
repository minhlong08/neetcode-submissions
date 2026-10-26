class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # Letter counts for s1 and for the current window of s2.
        # Index 0 = 'a', 1 = 'b', ..., 25 = 'z'.
        need = [0] * 26
        window = [0] * 26
        for i in range(n):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # Number of letters whose counts agree between need and window.
        # The window is a permutation of s1 exactly when all 26 agree.
        matches = 0
        for i in range(26):
            if need[i] == window[i]:
                matches += 1

        # Slide the window one step at a time.
        # s2[r] enters on the right, s2[r - n] leaves on the left.
        for r in range(n, m):
            if matches == 26:
                return True

            # --- Add the incoming character ---
            idx = ord(s2[r]) - ord('a')
            if window[idx] == need[idx]:
                matches -= 1          # it matched before; about to change
            window[idx] += 1
            if window[idx] == need[idx]:
                matches += 1          # it matches after the change

            # --- Remove the outgoing character ---
            idx = ord(s2[r - n]) - ord('a')
            if window[idx] == need[idx]:
                matches -= 1          # it matched before; about to change
            window[idx] -= 1
            if window[idx] == need[idx]:
                matches += 1          # it matches after the change

        # The loop checks before each slide, so check the last window here.
        return matches == 26