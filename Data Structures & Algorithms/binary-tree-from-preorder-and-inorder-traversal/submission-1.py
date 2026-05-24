# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case if either of them are empty
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])  # get the root our new tree
        mid = inorder.index(preorder[0])  # midpoint of our new tree to be used as reference later

        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])  # build left subtree as root.left
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])  # build right subtree as root.right

        return root
        