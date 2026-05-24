class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        # now heapify it
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            largest = heapq.heappop(maxHeap)
            second_largest = heapq.heappop(maxHeap)

            if largest == second_largest:
                continue
            elif largest > second_largest:
                continue
            elif largest < second_largest:
                heapq.heappush(maxHeap, largest - second_largest)
            
        maxHeap.append(0)
        return abs(maxHeap[0])