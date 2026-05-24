# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:  # iterating until fast and fast.next are both not null
            slow = slow.next
            fast = fast.next.next

        # Now we reverse the second half. Remember that second half starts right after the node slow is pointing at.
        second = slow.next
        prev = None
        slow.next = None  # instead of start of second half its now None, meaning we just broke the link and now its a separate link.
        while second:  # while second half is not empty we keep iterating
            # reversing the second here:
            tmp = second.next
            second.next = prev  # reversing thats why
            prev = second
            second = tmp  # now for next iteration, second will be original's next so we can continue reversing links.
        
        # Merging the two halfs now:
        first = head
        second = prev  # this is where the second half is actually starting from
        while second:  # we keep going until the second half of the list is not null, second beacause we know this could be the smaller half.
            tmp1, tmp2 = first.next, second.next  # tmp variables will hold the nexts as thats the link we are modifying.
            first.next = second  # first node will now point to node at the start of the second half
            second.next = tmp1  #  first node in the second half will now point to the second node from first half
            # This was it for merging, now just switching the pointers
            first = tmp1
            second = tmp2

"""We are not returning anything here just rearanging the nodes"""