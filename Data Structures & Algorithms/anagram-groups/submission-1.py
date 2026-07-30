class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashlen = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            hashlen[tuple(count)].append(s)

        res = []
        for key in hashlen:
            res.append(hashlen[key])

        return res
