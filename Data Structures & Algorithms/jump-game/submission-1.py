class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        # start with goal being n - 1
        goal = n - 1
        
        # if from current index can reach goal
        # update goal to be the current index
        for cur in range(goal - 1, -1, -1):
            if cur + nums[cur] >= goal:
                goal = cur

        # if final goal is 0 then we can reach the end
        return goal == 0
        