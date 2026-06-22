

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                lastBrack = stack.pop()

                if matching[char] != lastBrack:
                    return False
                
        
        return len(stack) == 0