# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS implemented again - this time dealing with the 
        logic demanded by the question"""

        q = collections.deque([root])
        res = []

        while q:
            rightSide = None  # in previous question here was Level = [] -- think why!
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node  # we assume node popped from left will now be right side
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:  # rightSide is being not treated as a list, rather a variable that holds the right most node at each level:
                res.append(rightSide.val)
        return res