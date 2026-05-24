class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

"""
for i, n in enumerate(nums):
    if n == target:
        return i
    
    return -1

This is another way to keep a track of index number in nums

"""