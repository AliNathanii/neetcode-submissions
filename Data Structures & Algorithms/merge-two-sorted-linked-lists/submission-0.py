# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # so that we dont need to worry about a list being an empty ie an edge case.
        tail = dummy  # initially the tail is just dummy ie empty

        while list1 and list2:  # meaning while both of our lists are not null or not empty.
            if list1.val < list2.val:
                tail.next = list1  # tail will now point at ie tail.next to l1 node as l1 contains smaller value than l2's value.
                list1 = list1.next  # update the l1 pointer to the next one.
            else:  # l2 node contains smaller value or equal value as l2.
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # we have to update our tail pouinter regardless of the condition thats why it is outside the if-else.

        # what if one of the lists is empty?
        if list1:  # if l1 is NON NULL:
            tail.next = list1
        elif list2:  # if l2 is NON NULL:
            tail.next = list2

        return dummy.next  # dummy is the empty list and its next will point at the new sorted linked list.
