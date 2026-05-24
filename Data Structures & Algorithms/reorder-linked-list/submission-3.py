# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # step 1 find the second half of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # we now have the pointers where we want to find the second half of the list ie right after slow
        
        # reverse this second half now
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        # prev will now be the reversed list, and not second (or curr as we call it sometimes)

        # now we will merge these two lists first and second - and first starts from the head while second starts from prev as we reversed the second part of the list above:
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1  # merging done, now we take care of moving the pointers
            first = tmp1  # move first and second now to their respective nexts ie tmp1 and tmp2
            second = tmp2