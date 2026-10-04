class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # The left portion is sorted
            if nums[l] <= nums[mid]:
                # In this portion the smallest is nums[l]
                # the largest is nums[mid]
                if target < nums[l]:
                    l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else: # nums[l] < target < nums[mid] -> continue search this portion
                    r = mid - 1
            # The right portion is sorted
            else:
                if target > nums[r]:
                    r = mid - 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1