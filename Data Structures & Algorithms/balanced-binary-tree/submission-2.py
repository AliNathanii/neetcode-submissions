# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # get the height of tree ie depth first search
        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            tree_depth = 1 + max(left_height, right_height)

            
            
            if abs(right_height - left_height) >= 2:
                return False

            if left_height is False or right_height is False:
                return False


            return tree_depth
        
        if root:
            return dfs(root) != False
        else:
            return True