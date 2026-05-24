class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # first use floyds algo to find where is the cycle, if it is in there:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        # next start another slow2 pointer from 0, and see when they meet (slow pointer remains unchanged from above)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:  # whereever they meet break the loop
                break
        # and then we can return any of the slow or slow2 pointer
        return slow