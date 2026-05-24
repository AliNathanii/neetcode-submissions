# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get height of right subtree, recursively
        # get height of left subtree, recursively
        # if their abs diff is 2 or more return False
        # else return True

        def dfs(root):
            if not root:
                return 0  # height of an empty tree which is 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            
            if left_height is False or right_height is False:
                return False  # Propagate False if any subtree is unbalanced
            
            if abs(right_height - left_height) >= 2:
                return False  # current node is unbalanced
            
            return 1 + max(left_height, right_height)  # Return height of current subtree
           
        if root:  # if the given root is not empty, apply dfs on root and return 
            return dfs(root) != False  # dfs(root) != False: imagine if dfs(root) returns 2 meaning the tree rooted at root is balanced and we get True returned. If dfs(root) returns False it evaluates to False, indicating the tree rooted at root is not balanced.
        else:  # if the given root is empty we return True as we can assume the tree is balanced
            return True


