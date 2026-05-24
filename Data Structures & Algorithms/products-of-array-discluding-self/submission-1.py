class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # initializing left and right product arrays as [1, 1, ,1 ,1 ...n]
        left_products = [1] * n
        right_products = [1] * n

        # computing the left products
        for i in range(1, n):
            left_products[i] = left_products[i -1] * nums[i-1]

        # computing the right products
        for i in range(n-2, -1, -1):  # n-2 because we wanna start iterating from the second to last index of the array, then -1 means the loop ends at the very last index (first if starting from the left) and then the second -1 means we move backwards from right to left ie in reverse!
            right_products[i] = right_products[i+1] * nums[i+1]

        # Finally compute the answer we want
        answer = [left_products[i] * right_products[i] for i in range(n)]
        # this is a concise way of creating a new list by iterating over a range and applying an operation to each element. 
        # In this case, it multiplies the elements at index i from left_products and right_products and collects the results in a new list.

        return answer


        