class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mem = defaultdict(int)
        for i in s:
            mem[i]+=1
        for i in t:
            mem[i]-=1
            if mem[i] < 0: return False
        return sum(mem.values()) == 0