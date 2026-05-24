# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # not important what value dummy holds but it must point to head as we are adding this right to the start
        left = dummy  # left pointer heads to dummy node.
        # initially right points to head but we keep shifting it until we find the corect node hence the following while loop:
        right = head
        while n > 0 and right:  # meaning while n is greater than 0 and right pointer node is not empty:
            right = right.next 
            n -= 1  # shift right by 1 and decrement n by 1 as well
        # by now we have found the correct right node we want!
        
        # keep shifting both pointers now until right reaches the end of the linked list.
        while right:
            right = right.next
            left = left.next

        # Now we wanna delete the node as well, we do this by updating left node's next pointer!
        left.next = left.next.next

        return dummy.next  # .next because we dont want to return dummy node. Also dummy because we know that dummy noded points to the head.