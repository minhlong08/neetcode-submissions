class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:    # in the left sorted portion
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:   # in the right unsorted portion
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else: # nums[mid] < target < nums[r]
                    l = mid + 1
        
        return -1