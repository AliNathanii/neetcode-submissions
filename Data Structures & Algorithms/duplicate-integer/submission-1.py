class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # sort the list first of all to have duplicates adjacent.
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False