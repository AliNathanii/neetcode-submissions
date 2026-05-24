"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not N  one else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Make new hashmap that will have old nodes as key and new nodes as value"""

        oldToNew = {}

        # Now start with dfs to process all the nodes
        def dfs(node):  # we will pass in a node evertime we call it
            if node in oldToNew:  # if we have already made a copy of the node we gave it
                return oldToNew[node]  # just return the copy (key's value) of that node from our hashmap
            
            # if not, then lets make a copy and store it in our hashmap
            copy = Node(node.val)
            oldToNew[node] = copy  # mapping the old node to our copy in oldToNew hasmap
            # then we also wanna make copy of every single neighbor of the nodee
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))  # dfs(nei) will return the copy we end up creating, and we will append that copy to our copy node's neighbors values!
            
            # at the end of our dfs, return the copy node that we just made in the current function call
            # we are basically taking a node and cloning it and cloning all its neighboers recursively
            return copy
        
        if node:  # if original node is not empty/None
            return dfs(node)
        else:
            None