# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            leftsubtree = dfs(root.left)
            rightsubtree = dfs(root.right)
            treedepth = 1 + max(leftsubtree, rightsubtree)
            if abs(rightsubtree - leftsubtree) >= 2:
                return False
            if rightsubtree is False or leftsubtree is False:
                return False
            return treedepth
        
        if root:
            return dfs(root) != False
        else:
            return True