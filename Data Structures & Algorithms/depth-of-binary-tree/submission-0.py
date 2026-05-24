# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Recursive Approach"""

        # Base case of recurive algorithm:
        if not root:
            return 0  # if root node is empty meaning no children so depth must be 0
        
        # At this point we know that depth is Not 0 and we do have children!
        left_depth = self.maxDepth(root.left)  # left subtree depth
        right_depth = self.maxDepth(root.right)  # right subtree depth

        # we add one because this is for the link/height/depth between the very top root node and its children
        return 1 + max(left_depth, right_depth)  