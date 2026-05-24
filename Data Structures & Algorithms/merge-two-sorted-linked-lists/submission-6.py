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
                tail.next = list1  # tail.next will point at list1 since it has a smaller value
                list1 = list1.next  # update list1 to its next to keep the traversal going
                tail = tail.next  # update tail to tail's next to keep the traversal going
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        
        # one of the lists got empty other one still has nodes left
        if list1:
            tail.next = list1  # make list 1 tail's next now
        elif list2:
            tail.next = list2

        return dummy.next