class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # frequency hashmap for s1
        freqS1 = {}
        for char in s1:
            freqS1[char] = freqS1.get(char,0) + 1
        
        # intialise freqency of s2 sliding window
        # the sliding window size is k = len(s1)
        k = len(s1)
        freqS2 = {}
        for char in s2[:k]:
            freqS2[char] = freqS2.get(char, 0) + 1

        if freqS1 == freqS2:
            return True
        
        for r in range(k, len(s2)):
            # add the incoming charater
            freqS2[s2[r]] = freqS2.get(s2[r], 0) + 1

            # remove the outgoing character
            out = s2[r - k]
            freqS2[out] -= 1
            if freqS2[out] == 0:
                del freqS2[out]

            # if 2 frequency map is equal -> return True
            if freqS1 == freqS2:
                return True

        return False