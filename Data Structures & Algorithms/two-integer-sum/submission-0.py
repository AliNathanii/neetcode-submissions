class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  # iterate over each element in the list.
            for j in range(i+1, len(nums)):  # iterate over each subsequentt elementt ie iterate over the very next one afetr i as for this for loop we start from index i+1.
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
"""This approach is brute force with time complexity O(n^2)"""