class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)  # Initialize the result array with 1s. This array will store the final products.

        for i in range(1, len(nums)):  # First pass: calculate prefix products. res[i] will store the product of all elements to the left of index i.
            res[i] = res[i-1] * nums[i-1]  # Multiply the previous prefix product by the element to the left of i.
        
        postfix = 1  # Initialize postfix product to 1. This will be used to calculate the product of elements to the right.
        
        # Second pass: calculate postfix products and update the result array. Iterate from the end of the array to the beginning.
        for i in range(len(nums)-1, -1, -1):  # this is how you start traversing from right to left ie end to start.
            res[i] *= postfix  # Multiply the current value in res (prefix product) by the postfix product.
            postfix *= nums[i]  # Update the postfix product by multiplying it by the current element.
        
        return res