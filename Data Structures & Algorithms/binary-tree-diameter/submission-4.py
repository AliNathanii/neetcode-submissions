# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = [0]  # to make res iterable we can have it as a list that only has one item 0 in it

        def dfs(root):
            if not root:
                return -1
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)
            tree_length = 1 + max(left_subtree, right_subtree)

            res[0] = max(res[0], 2 + left_subtree + right_subtree)  # the first item of res list is all we care about and access, and can access!

            return tree_length  # calculate and return tree_length to make the recursive calls for subtree lengths work
        
        dfs(root)
        return res[0]
        