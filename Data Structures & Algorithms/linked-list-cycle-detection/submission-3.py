# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next  # moving slow pointer here
            fast = fast.next.next  # moving the fast pointer now
            if slow == fast:
                return True
        
        return False


"""
Slow and Fast both start from the head. But slow iterates to the 
next node while fast iterate to the next to the next node! Skips one basically.
And then if slow == fast return True otherwise once the while loop ends
return False else that means the two pointers were never equal to
each other at any point.
Important: We keep iterating while fast and node next to fast are not
empty, fast pointer is the bottleneck as it is the one ahead and slow
pointer is behind.
TC = O(N) and SC = O(1)
"""