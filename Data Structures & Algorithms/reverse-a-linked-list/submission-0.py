# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # taking a two pointer approach
        prev, curr = None, head  # since curr in head so prev ie before head has to be null

        while curr:  # means while curr is Not empty. We do this as we wanna get to the end of the array.
            nxt = curr.next  # this holds the curr.next value as we will change curr.next in the next line but we need this value.
            curr.next = prev  # curr.next now points to previous (remember we wanna reverse the array)d
            prev = curr  # previous now curr so this is also reversed
            curr = nxt  # and now we point curr to curr.next (original one) so that in the next iteration of while loop we can keep reversing.
        return prev  # curr.next = prev ie prev will hold the reversed string once the while loop ends.