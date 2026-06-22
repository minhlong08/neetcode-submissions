class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        non_zero_product = 1
        count_zero = 0
        for num in nums:
            product = product * num
            if num != 0:
                non_zero_product = non_zero_product * num
            if num == 0:
                count_zero += 1

        res = []

        for num in nums:
            if num == 0 and count_zero == 1:
                res.append(non_zero_product)
            elif num == 0 and count_zero > 1:
                res.append(0)
            else:
                new_product = int(product / num)
                res.append(new_product)
        
        return res
        