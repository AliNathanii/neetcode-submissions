class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # initially the entire input array is under consideration.

        while l <= r:  # using a while loop as we want the loop to end only when we find the answer or that there is no answer at all.

            m = (l + r) // 2  # // because we want it rounded down and not whole number. 
            
            if nums[m] > target:  # if the value at index mid is Greater than target value then we move r our right pointer as we wanna look at the all the items to the Left of the mid!
                r = m - 1
            elif nums[m] < target:
                l = m + 1  # in this case we move left pointer to the right hence m + 1 is the new left pointer.
            else:  # this must mean we have found the match!
                return m
        return -1  # loop has ended and we found no match ie no answer therefore returning -1.
