# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """Preorder traveral using DFS -- we need to build a new function
        for dfs in case we wanna give it more args than the current function."""

        def dfs(node, maxVal):
            # base case if the tree is empty:
            if not node:
                return 0  # empty tree meaning no good nodes!
            
            if node.val >= maxVal:  # Determine if the current node is a 'good' node, ie its value is greater than or equal to maxVal
                res = 1  # this is node is "good" so we start the count at 1
            else:
                res = 0
     
            maxVal = max(maxVal, node.val)  # Update maxVal to be the maximum value seen so far along this path.
            
            res += dfs(node.left, maxVal)  # recursively counting the "good" nodes in the left subtree
            res += dfs(node.right, maxVal)  # recursively counting the "good" nodes in the right subtree
            return res
        
        return dfs(root, root.val)