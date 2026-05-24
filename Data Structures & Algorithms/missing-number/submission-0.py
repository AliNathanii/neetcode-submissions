class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Using a Hashset"""
        num_set = set(nums)

        for i in range(len(nums) + 1):  # we wanna include upto n
            if i not in num_set:  # i and not nums[i] as we know that the list nums is sorted [0, n] with just one number missing in between
                return i  # return the number i if it is not in our num_set
            
        return -1
    
# Time Complexity: O(n)
# Space Complexity: O(n)