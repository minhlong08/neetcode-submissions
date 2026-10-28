class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque() # store (temp, index)
        res = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = index - stackInd
            stack.append((t, index))
        return res