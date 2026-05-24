class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length +=1
                longest = max(length, longest)  # length is the current iteration's length value and longest was the previous iteration's length value

        return longest