# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None  # starting our two pointers curr and prev
        while curr:
            next_node = curr.next  # temp variable that will later be used to keep the process going
            curr.next = prev  # curr.next pointer will now point to prev pointer (POINTER REVERSED)
            prev = curr  # prev pointer will now point to curr (PREV POINTER ALSO REVERSED)
            curr = next_node  # to keep the process going

        return prev