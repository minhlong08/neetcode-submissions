class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        size, res = [], ""
        for s in strs:
            size.append(len(s))
        
        for sz in size:
            res += f"{sz},"
        res += "#"

        for s in strs:
            res += s
        
        return res

    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        sizes, res, i = [], [], 0 

        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        
        i += 1

        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz
        return res

