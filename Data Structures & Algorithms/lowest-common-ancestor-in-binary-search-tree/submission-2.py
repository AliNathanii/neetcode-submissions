# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """We start traversing from the given root as cur, and move our cur 
        according to the condition being met. While loop continues as long as 
        cur is not empty or we return cur value at some point"""

        cur = root

        while cur:  # we are guaranteed that there exits a solution at some point
            # if p value and q value are both greater than the cur ie root value
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right  # in this case we go down the right subtree

            # if p value and q value are both smaller than the curr root value
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left  # in this case we go down the left subtree (remember this is a binary search tree so the values are ordered)

            # if none of the above statements come in effect meaning we found our answer!
            else:
                return cur
        
        # nothing being returned outside while loop we are guaranteed that this is gonna execute at some point