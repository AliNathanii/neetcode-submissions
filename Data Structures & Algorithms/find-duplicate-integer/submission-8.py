class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Floyd's algorithm is being used here"""
                
        # Phase 1 of the algorithm; Detecting a Cycle:
        slow, fast = 0, 0  # both pointers initialized at index 0.
        while True:
            slow = nums[slow]  # slow pointer pointing at the number inside list at index [slow].
            fast = nums[nums[fast]]  # fast pointer moves two steps at a time. No need to increment directly by adding 1 each time. This is how incrementingg is done here, thanks to While True above.
            if slow == fast:  # once the two pointers meet we break the cycle. 
                break
            
        # Phase 2 of the algorithm; Finding the Cycle Entry Point:
        slow2 = 0  # slow2 pointer starts from the start of the array.
        while True:
            slow = nums[slow]  # slow pointer continues from where it left off above!
            slow2 = nums[slow2]  
            if slow == slow2:  # wherever they meet slow and slow2 thats where the cycle's entry point is! Thus we can return slow or slow2.
                break  # or we could just return slow/slow2 here.

        return slow  # we could also just return slow2