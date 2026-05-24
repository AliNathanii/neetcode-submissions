class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:  #  be sure to have this else OUTSIDE the for loop to be only executed once we have iterated through all items of the list.
            return -1

"""TC is O(n) and not O(logn), next submission has binary search
which has TC of O(logn)d."""