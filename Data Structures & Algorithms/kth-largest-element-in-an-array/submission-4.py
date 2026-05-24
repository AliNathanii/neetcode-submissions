class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)  # log n time complexity of the sorting algorithm!
        print(nums)
        return nums[k - 1]