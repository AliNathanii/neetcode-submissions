# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)  # append that nodes value to level if node is not empty
                    q.append(node.left)  # fill the q to keep it going for that level until breadth is complete
                    q.append(node.right)
            if level:  # for this while iteration, if level is not empty then append that level's node values to our res list
                res.append(level)
        return res