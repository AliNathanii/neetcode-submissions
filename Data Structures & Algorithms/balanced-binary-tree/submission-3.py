# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # get the heights of each subtree first 
        def dfs(root):
            if not root:
                return 0
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)
            tree_length = 1 + max(left_subtree, right_subtree)

            if abs(right_subtree - left_subtree) >= 2:
                return False
            
            if right_subtree is False or left_subtree is False:
                return False

            return tree_length

        if root:
            return dfs(root) != False
        else:
            return True  # empty tree is considered a BST!