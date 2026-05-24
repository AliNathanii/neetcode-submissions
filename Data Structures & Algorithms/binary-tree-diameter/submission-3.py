# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        def dfs(root):
            if not root:
                return -1  # with diameter of BST we return -1 so the math works (this is done when caluclating diameter, not during the depth question)
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)
            tree_depth = 1 + max(left_subtree, right_subtree)

            res[0] = max(res[0], 2 + left_subtree + right_subtree)

            return tree_depth
        
        dfs(root)
        return res[0]
        