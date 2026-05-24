# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        while q:
            qlen = len(q)
            rightNode = None  # new for each breadth level
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightNode:  # after we have looped through all items in that particular level (one while loop iteration for one level), only then we check if rightNode was empty or not
                res.append(rightNode.val)
        
        return res
