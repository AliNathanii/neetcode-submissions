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

        curr = head

        # this while loop only creates copy node of curr and in the hashmap, adds copy as key for curr. Keeps going till the end:
        while curr:  # creates a copy node of curr node's value, and stores it into the dict with curr as key and new node as the value
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        # this while loop get copy node from hashmap for curr, and adjust its next pointer and ranodm pointer to the key in hashmaps' respective pointers
        curr = head
        while curr:  # gets the copy node from dict at curr, adjusts its .next and .random pointers wrt to curr in oldToCopy dict
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        # return the head node from the hashmap oldToCopy
        return oldToCopy[head]