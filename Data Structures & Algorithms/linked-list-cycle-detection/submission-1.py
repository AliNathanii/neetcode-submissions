# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current:
            if current.val in visited:
                return True
            visited.add(current.val)
            current = current.next
        return False

"""We build a new set that we append to the values of nodes as we
traverse through them. If the value is found to be already in the set,
we return True. After the while loop ends meaning no cycle/similar 
value was found meaning there was no link therefore we return False.
current = current.next is how you traverse through the linked list.
TC = O(N) and SC = O(N) as we are creating a new set that will have n 
number of items.
To improve the SC we can use two pointer, slow and fast pointer approach."""