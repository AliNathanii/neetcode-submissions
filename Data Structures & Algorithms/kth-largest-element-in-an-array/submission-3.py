class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for n in nums[k:]:
            if n > minHeap[0]:
                heapq.heapreplace(minHeap, n)
        
        return minHeap[0]