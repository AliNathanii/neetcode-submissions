class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """This is the brute force option. Using for loop with
        enumerate we can keep track of both index and the number.
        Time complexity O(n)"""

        for index, num in enumerate(nums):
            if num == target:
                return index
        return -1