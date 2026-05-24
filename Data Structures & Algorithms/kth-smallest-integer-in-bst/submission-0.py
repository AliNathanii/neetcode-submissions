# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Get the sorted values of the BST in a list and then 
        simply get the kth element from that list"""

        res = []  # this is the list to which we will append traversed node values

        # IN ORDER TRAVERSAL ie Left Node -> Root -> Right Node this will get us a sorted list
        def in_order(tree_root, res):
            if tree_root:
                in_order(tree_root.left, res)
                res.append(tree_root.val)
                in_order(tree_root.right, res)
            
            # by the end of this if statement in the function res will contain the values of tree, sorted.
        

        
        in_order(root, res)

        return res[k - 1]
