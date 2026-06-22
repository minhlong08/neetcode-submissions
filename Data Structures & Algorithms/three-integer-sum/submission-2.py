class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # For each index i in the sorted array, we need to find
        # index j, k such that -nums[i] = nums[j] + nums[k]
        # Uses 2 pointers: j at the start of the sorted array, k at
        # the end of the sorted array
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue # dont reuse the first position
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l = l + 1
                elif threeSum > 0:
                    r = r - 1
                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res