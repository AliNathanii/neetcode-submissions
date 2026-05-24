# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """DFS to get the height"""

        # base case:
        if not root:
            return 0
        
        # moving on:
        left_depth = self.maxDepth(root.left)  # will be 0 first and return statement will add 1. Then will be 2 and return statement will make it 3 if base case still not met...
        right_depth = self.maxDepth(root.right)

        # once we have left and right depth, find tree depth by adding 1 to either one of their max
        tree_depth = 1 + max(left_depth, right_depth)  

        return tree_depth