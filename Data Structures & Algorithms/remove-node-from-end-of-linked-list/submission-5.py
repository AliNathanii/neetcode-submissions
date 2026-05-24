# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0 and right:  # get the right pointer to point at the node we wanna remove
            right = right.next
            n -= 1
        
        while right:  # bring left pointer such that its next pointer points as node we wanna remove
            right = right.next
            left = left.next
        
        left.next = left.next.next  # remove left.next node!

        return dummy.next