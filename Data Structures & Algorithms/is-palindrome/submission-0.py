class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(c for c in s if c.isalnum()).lower()

        j = len(string) - 1
        for i in range(len(string)//2):
            if string[i] != string[j]:
                return False
            j = j - 1
        
        return True