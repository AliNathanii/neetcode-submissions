class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # build a minHeap with k largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)  # minHeap list converted to a Heap (minheap automatically)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # keep popping/removing items from our self.minHeap until the length is the same as k


    def add(self, val: int) -> int:
        # add the value in our heap
        heapq.heappush(self.minHeap, val)
        # if length exceeds k just pop the smallest value (edge case)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  # first item in  minheap is always the smallest one thus we return it by indexing
