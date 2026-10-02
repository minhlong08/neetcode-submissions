class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ','')
        cleaned_s = "".join(char for char in s if char.isalnum())
        l = 0
        r = len(cleaned_s) - 1

        while l < r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l = l + 1
            r = r - 1

        return True