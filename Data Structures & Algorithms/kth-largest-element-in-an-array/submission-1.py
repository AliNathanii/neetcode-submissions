class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Solving by sorting it"""
        nums.sort(reverse = True)  # sort it in Descending Order as we want the kth Largest Element!
        return nums[k-1]