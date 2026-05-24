class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Brute Force solution"""

        our_min = nums[0]

        for num in nums:
            our_min = min(num, our_min)

        return our_min