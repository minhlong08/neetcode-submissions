class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 in nums_set:
                continue
            
            next_num = num + 1
            seq_len = 1
            while next_num in nums_set:
                seq_len += 1
                next_num += 1
            
            if seq_len > max_seq:
                max_seq = seq_len
        
        return max_seq