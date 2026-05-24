class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)  # Key: the item/value in the list. Value: its count!
        maxHeap = [-cnt for cnt in count.values()]  # adding all values in maxHeap as -ve so now largest value will be in the root of maxHeap
        heapq.heapify(maxHeap)  # convert maxHeap from a list to a heap!

        time = 0  # initially time will be 0
        q = deque()  # why not collections.deque()? This queue will contain items as a pair [-cnt, idleTime]

        while maxHeap or q:  # as long as our maxHeap or the queue is not empty:
            time += 1  # increment time each iteration

            if maxHeap:  # if the maxHeap contains task, we pop it and reduce the count by 1. Values are negative thats why we add 1 to decrement it.
                cnt = 1 + heapq.heappop(maxHeap)  # pop the task with highest count ie largest negative value
                if cnt:  # if there are still instances of this cnt left:
                    q.append([cnt, time + n])  # append to our queue! n is the cool down time given as parameter

            # Check if the task at the front of the queue has completed its cooldown
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])  # Push the task back into the heap
            
        return time  # return the total time taken!

"""
Main Loop: Continue the loop until both the max-heap and the queue are empty:
Increment the time counter at each iteration.
If there are tasks in the max-heap, pop the task with the highest frequency (largest negative value) and decrement its count.
If the task still needs to be executed (count not zero), add it to the queue along with the time it will be eligible to run again (current time + cooldown period).
Check if any task in the front of the queue has completed its cooldown. If so, push it back into the max-heap.
-- so we are essentially using queue to keep track of tasks during their cooldown period!
"""