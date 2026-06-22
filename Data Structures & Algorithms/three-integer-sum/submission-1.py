class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        sort_nums = sorted(nums)

        # For each index i in the sorted array, we need to find
        # index j, k such that -nums[i] = nums[j] + nums[k]
        # Uses 2 pointers: j at the start of the sorted array, k at
        # the end of the sorted array
        for i, num in enumerate(sort_nums):
            target = num * -1

            j = i + 1
            k = len(sort_nums) - 1

            while j < k:
                current_sum = sort_nums[j] + sort_nums[k]
                if current_sum > target:
                    k = k - 1
                elif current_sum < target:
                    j = j + 1
                else: # current_sum == target
                    triplets = (sort_nums[i], sort_nums[j], sort_nums[k])

                    if triplets not in seen:
                        seen.add(triplets)
                        res.append(list(triplets))

                    j += 1
                    k -= 1


        return res