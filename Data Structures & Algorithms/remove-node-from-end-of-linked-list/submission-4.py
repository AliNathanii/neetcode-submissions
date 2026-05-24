# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # be sure to initialize dummy as pointing to head only that way it is actually connected to our list
        left, right = dummy, head
        while n > 0 and right:  # by the end of this loop, right pointer will point at the node n we wanna remove
            right = right.next
            n -= 1
        while right:  # by the end of this loop right will point at last node and left will point at the node one before we wanna remove
            right = right.next
            left = left.next
        left.next = left.next.next  # removing the nth node from end
        return dummy.next  # return dummy.next as dummy is just dummy it points at the head!
"""
Our approach:
1. Initialize two pointers, l starting at dummy and r starting at the head
2. Have a while loop that ends with right pointer at the node at n (right is moved and n is decremented at each iteration)
3. Now while right, keep moving left to left.next and right to right.next. By the end, left.next will point at n! (not left itself)
4. Remove nth node by left.next = left.next.next
5. Finally we can return dummy.next (remember we return dummy.next and not dummy)
"""