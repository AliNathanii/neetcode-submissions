# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Brute Force TC O(n)"""
        # get the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # now that we have the length, get the node position we wanna remove
        node_to_remove = length - n

        # edge csae if n == 0 ie head needs to be removed
        if node_to_remove == 0:
            return head.next
        
        # traverse to the node JUST BEFORE that wed need to remove
        curr = head
        for i in range(node_to_remove - 1):
            curr = curr.next
        
        # curr now points to the node JUST BEFORE the node that needs to be removed and we will change curr.next now!
        curr.next = curr.next.next

        return head