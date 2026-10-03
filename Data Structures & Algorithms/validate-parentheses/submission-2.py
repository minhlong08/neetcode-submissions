class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(','{','[']
        closing = [')','}',']']

        for c in s:
            if c in opening:
                stack.insert(0,c)
            elif c in closing:
                if len(stack) == 0:
                    return False
                print('closing brack:', c)
                print('current stack', stack)
                matching = stack.pop(0)
                if c == ')' and matching != '(':
                    return False
                elif c == '}' and matching != '{':
                    return False
                elif c == ']' and matching != '[':
                    return False
        
        return len(stack) == 0