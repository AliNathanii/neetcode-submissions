# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Check if subRoot is a subtree of root."""

        def sameTree(root, subroot):
            """Check if two binary trees are identical."""
            if not root and not subroot:  # both are empty, they are the same!
                return True
            if root and subroot and root.val == subroot.val:  # both not empty and values match
                return (sameTree(root.left, subroot.left) and sameTree(root.right, subroot.right))  # True will be returned if they are the same otherwise False
            return False  # if none of the conditions match, they are not the same

        # Edge cases (back to isSubtree function)
        if root and not subRoot:  # empty subtree is a subtree
            return True
        if not root:  # non-empty subtree cannot be a subtree of an empty tree
            return False
        # Check if root and subRoot are the same or if subRoot is a subtree of either child:
        return (sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
