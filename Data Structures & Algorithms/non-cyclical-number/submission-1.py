class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            curSum = 0
            for c in str(n):
                curSum += int(c) ** 2
            
            if curSum == 1:
                return True
            else:
                n = curSum
        
        return False