# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """We will use revcursive approach to solve this,
        Depth First Search Algorithm used"""

        if not root:  # Base case for recursives if root is empty just return None
            return None
        
        # Now we swap the childrens here, since thats what inverting is:
        tmp = root.left  # tmp is the variable that will hold root.left's current value before we change it
        root.left = root.right
        root.right = tmp

        # Above we swapped the children, now we make the recursive call to keep it going until root is empty
        self.invertTree(root.right)  # inverting the right subtree (postorder, but it also doesnt matter)
        self.invertTree(root.left)  # inverting the left subtree

        return root  # returning root as thats the tree's root that has everythong connected to it