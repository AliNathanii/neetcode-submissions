class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Optimal Solution using 2 pointers slow and fast"""

        # Detecting there is a cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2  # or you can return slow as well they are pointing at the same thing