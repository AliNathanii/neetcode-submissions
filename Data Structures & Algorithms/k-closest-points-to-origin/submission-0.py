class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Get the dist, and add it to our minHeap in [] that way dist, x and y are all
        there are as a single value minHeap list. Afte appended heapify minHeap and 
        keep popping from it k times meaning until given k becomes 0 as we decrement it per
        iteration of the while loop. Be sure to append x, y from popped values and then 
        return that appended res list."""

        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)  # smallest dist value will be put in the respective place when we apply heapify.
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # as we pop, points with smallest dist values will be popped!
            res.append([x, y])
            k -= 1
        
        return res

"""Keep everything the same but in the MinHeap have the numbers negative,
return abs value and technically you will have the points Furthest from the
origin!"""