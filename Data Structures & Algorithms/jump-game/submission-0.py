class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        goal = n - 1
        
        for cur in range(goal - 1, -1, -1):
            if cur + nums[cur] >= goal:
                goal = cur

        return goal == 0
        