class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indexMap = {}
        for i, num in enumerate(nums):
            indexMap[num] = i

        res = set()
        for idx1, num1 in enumerate(nums):
            target1 = 0 - num1
            for idx2, num2 in enumerate(nums):
                if idx2 == idx1:
                    continue
                target2 = target1 - num2
                if target2 in indexMap and idx2 != indexMap[target2] and idx1 != indexMap[target2]:
                    candidate = tuple(sorted([num1, num2, target2]))
                    if candidate not in res:
                        res.add(candidate)
        res2 = list(res)
        return [list(i) for i in res2]