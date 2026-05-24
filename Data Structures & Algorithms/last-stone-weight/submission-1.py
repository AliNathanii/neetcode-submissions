class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # make all stone values negative to implement maxHeap
        stones = [-s for s in stones]

        # convert list stones into a heap
        heapq.heapify(stones)

        while len(stones) > 1:
            largest_stone = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if largest_stone == second_largest:  # given condition in question, if this happens just move on to the next iteration
                continue
            elif largest_stone > second_largest:  # again you can move on to the next iteration
                continue
            elif largest_stone < second_largest:  # in case y is greater than x:
                heapq.heappush(stones, largest_stone - second_largest)
        
        stones.append(0)  # edge case in case the list was empty
        return abs(stones[0])

        