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
        oldToCopy = {None: None}  # None: None to avoid no node edge case. Otherwise we could have just initiated an empty {}

        curr = head
        while curr:  # making new node for each node in the original list and maps each original node to its copy in the dict oldToCopy
            copy = Node(curr.val)  # copy is the copy node and it contains the same value as the current node's value
            oldToCopy[curr] = copy  # key: original node, value: the copy node
            curr = curr.next  # to keep traversing to the next node and repeat the above steps with them
        
        curr = head
        while curr:  # Uses the oldToCopy dictionary to link the next and random pointers of the copied nodes correctly.
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]
