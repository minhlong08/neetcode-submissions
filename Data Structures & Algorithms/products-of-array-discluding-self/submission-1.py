class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        product_prefix = 1
        # iterate from left to right, storing the product of
        # all number before the current index
        prefix.append(product_prefix)
        for i in range(1,len(nums)):
            product_prefix *= nums[i-1]
            prefix.append(product_prefix)

        product_suffix = 1
        # iterate from right to left, storing the product of
        # all number before the current index
        suffix.append(product_suffix)
        for i in range(len(nums) - 2, -1 , -1):
            product_suffix *= nums[i+1]
            suffix.insert(0, product_suffix)

        print(prefix)
        print(suffix)
        res = [x*y for x,y in zip(prefix, suffix)]

        return res