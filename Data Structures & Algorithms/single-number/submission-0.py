class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Time complexity O(1) and Space Complexity O(1)"""
        
        # We make use of XOR ^
        # If two bits are same, it will give 0
        # If they are different, it will give the different bit! (not just 0 and 1)

        res = 0
        for n in nums:  # iterate through each item in nums
            res = res ^ n  # res = previous res value (initalized as 0) XORed by current item in n
        return res  # as the loop ends return res. It will be 0 if values occured twice, else it'll return that one value as res that occured only once
