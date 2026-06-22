class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]

        #  creating a list where the index represents a frequency, 
        # and at each index we store all numbers that 
        # appear exactly that many times.
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res