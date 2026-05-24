# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the second half of the linked list -- slow and fast pointer approach
        slow, fast = head, head.next
        while fast and fast.next:  # continue iterating until fast and fast.next both are not null
            slow = slow.next
            fast = fast.next.next
        # slow.next will now point at the head of the second half of the linked list

        # reverse the second half now
        second = slow.next
        prev = None  # to break the links and create a new reversed second list
        slow.next = None

        while second:
            temp = second.next
            second.next = prev  # second.next now points to prev
            prev = second  # prev will now point at head of second list to keep the cycle going
            second = temp  # second is now what second.next was to keep the cycle going
        # prev by the end will become head of second list

        # Merge the two lists now
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # Merger done, now move the pointers of the heads, to their nexts to keep the cycle going:
            first = tmp1
            second = tmp2

