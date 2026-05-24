"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]  # return the copy node 
            copy = Node(node.val)
            oldtonew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))  # what to append in copy.neighbors? Well whatever node dfs(nei) returns!
            
            return copy  # you wann return the copy node eventually
        
        if node:
            return dfs(node)
        else:
            return None