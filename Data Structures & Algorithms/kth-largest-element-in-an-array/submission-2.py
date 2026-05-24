class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """"Using a minHeap in this example"""
        minHeap = nums[:k]  # add all the items from nums list to minHeap list upto but excluding k.

        heapq.heapify(minHeap)  # convert minHeap list to a heap!

        # Process the remaining elements ie all those numbers including and after k:
        for num in nums[k:]:  
            if num > minHeap[0]:  # if this number is larger than smallest number in minHeap at [0] then we replace the root ie that number with num!
                heapq.heapreplace(minHeap, num)
            
        return minHeap[0]  # By the end, root of minHeap with hold the Kth largest element in the original array!
        
        
"""
The algorithm starts by initializing a min-heap with the first k elements of the given array, which is accomplished by creating a list of these elements and using the heapq.heapify function to transform it into a min-heap. 
This ensures that the smallest element among these k elements is always at the root of the heap. 
Next, the algorithm iterates through the remaining elements of the array, starting from the kth element. For each of these elements, it compares the element with the root of the heap (the smallest element in the heap). 
If the current element is larger than the root, it replaces the root with this element using heapq.heapreplace, thereby maintaining the heap property. 
By the end of this process, the root of the heap holds the kth largest element in the array. 
The algorithm then returns the root of the heap as the result, which is the kth largest element in the original array.
"""