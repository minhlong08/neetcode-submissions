class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for key, value in sorted(count.items(), key = lambda x: x[1], reverse = True):
            result.append(key)
        
        return result[:k]