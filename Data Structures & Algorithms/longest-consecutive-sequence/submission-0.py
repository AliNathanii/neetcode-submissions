class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # nums array converted to set here.
        longest = 0  # initially longest consecutive sequence is 0.

        for n in nums:  # iterating through the nums array.
            if (n-1) not in numSet:  # check if it is start of a sequence. ie if this number does not have a left neighbor.
                length = 0  # since it doesnt, now we wanna find the length of this sequence.
                while (n + length) in numSet:  # this will check the current number. While the current number is not in the set, we increase length by one and then move on to the next number!
                    length += 1
                longest = max(length, longest)

        return longest