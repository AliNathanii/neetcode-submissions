# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # INORDER Traversal can be performed as its a BST 
        # and INORDER Traveral goes like Left -> Root -> Right

        res = []

        def in_order(node, res):
            if node:  # if the node is not empty
                in_order(node.left, res)
                res.append(node.val)  # process the value of the node we just accessed above
                in_order(node.right, res)
        
        in_order(root, res)
        return res[k -1]
            