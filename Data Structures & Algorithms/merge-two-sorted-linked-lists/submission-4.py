# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # if above condition met, tail's (dummy's) next will point at list 1 ie list 1 ' s head!
                list1 = list1.next  # list 1 will then point at list1' next
                tail = tail.next  # and for next iteration, tail will become tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

        if list1:  # if list 1 is not empty but list 2 is:
            tail.next = list1  # tail's next pointer will point at List 1's head
        elif list2:  # or this condition is to be checked for
            tail.next = list2

        return dummy.next