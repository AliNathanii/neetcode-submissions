class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        left_products = [1] * n  # left productt array initialized
        right_products = [1] * n  # right product array initialized 

        for i in range(1, n):  # add left products in left_products array
            left_products[i] = left_products[i -1 ] * nums[i - 1]  # this is how we do that
        
        for i in range(n-2, -1, -1):  # add right products in right_products array
            right_products[i] = right_products[i + 1] * nums[i + 1]  # this is how we do that

        res = [left_products[i] * right_products[i] for i in range(n)]  # multiply their values at i for i in range(n) and store all the products in a new array called res
        return res