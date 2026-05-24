# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """The diameter of a binary tree is the length of the longest path between any two nodes. 
        This path can pass through the root or any other node."""
        res = [0]  # this is the global variable that will be returned

        def dfs(root): 
            if not root:  # if the root is empty:
                return -1  # height is NOT 0 as that happens when root is not empty but has no children! When root is empty, there is basically no tree hence -1 height
            left = dfs(root.left)  # recursively finding the height of the left subtree.
            right = dfs(root.right)  # recursively finding the height of the right subtree.
            # Update the maximum diameter found so far:
            res[0] = max(res[0], 2 + left + right)  # this ensures that res[0] always holds the maximum diameter found. And, the formula 2 + left + right calculates the total number of edges on the path passing through the node
                                                    # left is the height of the left tree, same for right, and 2 accounts for the 2 edges connecting the current node to its children

            return 1 + max(left, right)  # this returns the height of the current subtree! If we only wanted to return the height like in previous questions we have done we just mention this line of the code and remove the above diameter formula!
        
        dfs(root)
        return res[0]  # why have the the res as res list and then return res[0]? Because having it as a list in python allows us to have it as an itterable object.
