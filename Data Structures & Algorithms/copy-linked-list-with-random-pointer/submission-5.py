"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None: None}
        # first copy the original node: copy node
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        # now fix the pointers
        curr = head
        while curr:
            node = oldToCopy[curr]  # get the node at curr key
            node.next = oldToCopy[curr.next]
            node.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]