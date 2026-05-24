# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # check each node and that keep calling it:
        def is_valid(root, left, right):
            if not root:
                return True
            if not(left < root.val < right):
                return False
            return is_valid(root.right, root.val, right) and is_valid(root.left, left, root.val)
        
        return is_valid(root, float("-inf"), float("inf"))