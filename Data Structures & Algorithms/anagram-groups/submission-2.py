class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashlen = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            
            hashlen[tuple(arr)].append(s)

        res = []

        for key in hashlen:
            res.append(hashlen[key])
        return res