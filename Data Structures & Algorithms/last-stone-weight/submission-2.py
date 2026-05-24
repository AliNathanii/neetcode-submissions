class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)  # made stones a maxHeap
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)
            if largest == second_largest:  # checking for conditions
                continue
            elif largest > second_largest:
                continue
            elif largest < second_largest:
                heapq.heappush(stones, largest - second_largest)
        stones.append(0)  # avoid edge case of an empty list
        return abs(stones[0])  # return the top of the maxHeap. abs as we made negatives earlier!