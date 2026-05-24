# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None  # starting our two pointers curr and prev
        while curr:
            next_node = curr.next  # Save the next node. (1.)
            curr.next = prev  # curr.next pointer will now point to prev pointer (POINTER REVERSED). (2.)
            prev = curr  # move the prev pointer Forward! (3.)
            curr = next_node  # to keep the process going. (3.)

        return prev

"""
For each node, we need to do the following:
1. Save the next node
2. Reverse the next pointer of current node to prev
3. Move prev and curr pointers forward!
"""