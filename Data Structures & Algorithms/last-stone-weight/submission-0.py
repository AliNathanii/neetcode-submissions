class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Just following the instructions and implementing them,
        no fancy algorithm used. Only tricky part: Simulating a 
        MaxHeap using a MinHeap as python doesnt support a Maxheap!"""

        stones = [-s for s in stones]  # stones is a new list of original stone memebers but all negative now
        heapq.heapify(stones)  # stones list now has been converted to a heap. MinHeap implemented but since values are negative we are using this is as MaxHeap

        # Now we can start our implementation:
        while len(stones) > 1:  # condition they specified in the question:
            largest_stone = heapq.heappop(stones)  # this will give us the largest stone in stones
            second_largest_stone = heapq.heappop(stones)  # this will now give us the second largest stone in stones
            if second_largest_stone > largest_stone:  # if this condition is not fullfilled we dont have to do anything, just let them be popped!
                heapq.heappush(stones, largest_stone - second_largest_stone)  # their difference is to be now added to our heap!
            
        stones.append(0)  # edge case in case the list given was empty! We used append and not push not maintain the heap property, and not mess with the order
        return abs(stones[0])  # return the last remaning stone which will be at the top! abs() because remember we used -ve values to use MinHeap as MaxHeap



        