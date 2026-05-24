# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base case: both nodes are empty so return True as they are the same
        if not p and not q:
            return True 
        
        # If one tree is empty and another one is filled:
        if not p or not q:
            return False  # we know instantly they are not the same

        # Compare current node's values, if different return False
        if p.val != q.val:
            return False
        
        # Recursvily apply this on left and right children of p and q
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # True will be returned if they are identical, False otherwise.