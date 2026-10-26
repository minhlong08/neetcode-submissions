class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum == target:
                return [l+1, r+1]
            elif curSum > target:
                r = r - 1
            else:
                l = l + 1
        
        # nothing found (should not happen according to the specifications)
        return []