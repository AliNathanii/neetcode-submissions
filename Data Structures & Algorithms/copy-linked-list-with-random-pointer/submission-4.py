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
        # lets make a copy node of each node and map it to a hashmap
        # key: original node, value: copy
        oldToCopy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)  # copy node built using curr's value
            oldToCopy[curr] = copy  # copy node mapped to curr node as the key
            curr = curr.next  # to keep the traversal going
        
        # now lets adjust the pointers of the copy node we just added in our hashmap as data 
        curr = head
        while curr:
            copy = oldToCopy[curr]  # access the copy node that was already mapped to curr node above
            copy.next = oldToCopy[curr.next]  # copy node's next will point to same as its key curr's next
            copy.random = oldToCopy[curr.random]  # copy node's random pointer will point to same as its key curr's random pointer
            curr = curr.next  # to keep the traversal going
        
        return oldToCopy[head]  # return value mapped to the head node in the hashmap