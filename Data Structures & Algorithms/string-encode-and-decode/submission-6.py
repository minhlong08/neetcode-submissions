class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        size, res = [], ""
        for s in strs:
            size.append(len(s))
        
        for sz in size:
            res += f"{sz},"
        res += "😊"

        for s in strs:
            res += s
        
        return res

    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []

        length_str = s.split("😊")[0]
        length_arr = [n for n in length_str.split(",") if n != ""]
        encode = s.split("😊")[1]

        print(s, encode)
        i = 0
        for sz in length_arr:
            res.append(encode[i: i + int(sz)])
            i += int(sz)
        
        return res

