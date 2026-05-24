# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # adding a dummy node as good practice
        curr = dummy  # starting our iteration from the dummy node, which is the new head?

        carry = 0  # carry is initially set to 0
        while l1 or l2 or carry:  # as long as any of the lists is not empty or carry is not 0
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            
            # calculating the new digit
            val = v1 + v2 + carry
            carry = val // 10  # to get the ones number
            val = val % 10  # to get the ones number
            curr.next = ListNode(val)  # adding this value to new node which we are creating here. So we start from dummy node and then keep adding new nodes here till the loop stops

            # updating the pointers here
            curr = curr.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        return dummy.next

"""
A better and shorter syntax for above if-else statements is:
    while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 
    
    cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

"""