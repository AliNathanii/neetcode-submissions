# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):  # left and right are the respective boundaries/limit for values at those positions
            # Base case if the node is empty:
            if not node:
                return True  # empty tree is a BST
            
            if not (node.val < right and node.val > left):  # if the right and left node dont follow the BST characterstic return False
                return False
            
            # Now we can make the recursive calls to this function and return what it would return
            # The left subtree must have values less than the current node's value.
            # Also validate the right subtree with updated constraints:
            # The right subtree must have values greater than the current node's value.
            # Notice that when applying on node.left, we update the right boundary as new limit will be node.val
            # and when applying on node.right, we update the left boundary as new limit will be node.val
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # Start the validation from the root node with initial constraints being negative and positive infinity.
        # we call our valid function by giving it the root and -ve and +ve infite as left and right boundaries respectively.
        return valid(root, float("-inf"), float("inf"))

