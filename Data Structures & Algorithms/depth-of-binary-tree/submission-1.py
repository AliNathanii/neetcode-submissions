# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Iterative DFS using a stack"""
        # start by initializing a stack that will contain a pair of node and depth ie node, depth.
        # initially it already contains the root node and depth ie 1
        stack = [[root, 1]]
        res = 0

        while stack:  # as long as the stack is not empty:
            node, depth = stack.pop()  # the pair popped from the stack root, depth will be assigned to node = root and depth = the int depth we initialized above

            if node:  # if node (we popped above) is not empty we:
                res = max(res, depth)  # assign res to max out of the current depth or already in res
                stack.append([node.left, depth + 1])  # append to stack left childrens and increment depth by 1
                stack.append([node.right, depth + 1])  # append to stack right childrens and increment depth by 1
        
        return res  # by this point res contains the maximum depth, either from left or/and right subtrees

"""
This is how you iteratively implement DFS:
1. Initialize a stack containing a pair of given root and depth which is initially 1 (but res = 0)
2. As long as its not empty, pop the stack and its values will be assigned to nodea and depth
3. if the popped node is not empty, we assig res to max value of present res and depth
4. Next we append to stack pair of left child node with depth + 1 as the second value of the pair
5. Next we do the same for right child node
6. Now we can return res as we assigned res to max of res and depth above
"""