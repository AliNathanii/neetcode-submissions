class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Efficient approach"""
        minHeap = nums[:k]
        heapq.heapify(minHeap)
        for n in nums[k:]:
            if n > minHeap[0]:  # if n is bigger than smallest item in minHeap meaning it has the potential and should be part of the Heap as everything else in the heap are greater than minHeap[0]
                heapq.heapreplace(minHeap, n)
        return minHeap[0]