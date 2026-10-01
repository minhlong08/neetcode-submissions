class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            curLen = ""
            j = i
            while s[j] != '#':
                curLen += s[j]
                j += 1

            length = int(curLen)
            i = j + 1
            res.append(s[i:i+length])
            i = i + length

        return res