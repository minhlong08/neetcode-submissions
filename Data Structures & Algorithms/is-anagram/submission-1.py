class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_str_1 = sorted(s)
        sorted_str_2 = sorted(t)

        i = 0
        j = 0

        if len(sorted_str_1) != len(sorted_str_2):
            return False

        while (i < len(sorted_str_1)):
            if sorted_str_1[i] != sorted_str_2[j]:
                return False
            i += 1
            j += 1
        
        return True
        