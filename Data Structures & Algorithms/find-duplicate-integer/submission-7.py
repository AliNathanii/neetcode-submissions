class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       """If we were allowed to modify the array by sorting it 
       TC would now be O(nlogn) logn due to sorting."""
       nums.sort()

       for i in range(len(nums) - 1):  # remember this is an array and not a linked list therefore we used [inedx] and not head or head.next()
        if nums[i] == nums[i + 1]:
            return nums[i]

