# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # make a dummy node and start the left pointer from there and right from head
        dummy = ListNode(0, head)  # be sure to initialize the head right as its value is 0 and NEXT WILL BE HEAD SO THAT DUMMY IS CONNECTED TO HEAD IE OUR MAIN LIST!
        left, right = dummy, head

        # move the right pointer to point to node we wanna remove
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # now move left to point right before the node we wanna remove
        while right:
            right = right.next
            left = left.next

        # we can now remove left.next
        left.next = left.next.next

        return dummy.next