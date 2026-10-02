class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Idea:
        # - Sort the array
        # 3 pointer i, l, r to find -nums[i] = nums[l] + nums[r]
        res = []
        nums.sort()

        for i, num1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: # dont reuse num1
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = num1 + nums[l] + nums[r]
                if threeSum < 0:
                    l = l + 1
                elif threeSum > 0:
                    r = r - 1
                else:
                    res.append([num1, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l - 1] and l < r:
                        l = l + 1
        return res

