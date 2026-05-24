class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Sum of array in range(len(input_array)) - Sum of input array"""

        res = len(nums)  # initializing as the length of nums and not 0, as we finally also wanna consider the final n value in the nums list

        for i in range(len(nums)):
            res += i - nums[i]  # add i but first subtract nums[i] from it first and add their difference to res
        return res  # final value of res will be the missing number!

# Time Complexity: O(n)
# Space Complexity: O(1)