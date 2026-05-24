# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:  # if both given nodes are greater than root, traverse to right subtree
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:  # if both given nodes are lesser than root, traverse to the left subtree
                curr = curr.left
            else:  # else this is the lowest common ancestor they share
                return curr

# what if the question asked for greatest common ancestor?
# in BST thats the root!!!