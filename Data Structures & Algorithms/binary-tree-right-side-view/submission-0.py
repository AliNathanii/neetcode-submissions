# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])  # list is already initiared with root in it so no need for level = [] list!

        while q:  # keep going as long as q is not empty
            rightSide = None  # get right side element from current, initally it is set to None
            qlen = len(q)  # current length of q

            for i in range(qlen):
                node = q.popleft()  # popping elements from the left and adding to the right
                if node:  # if node is not null
                    rightSide = node  # update our rightSide to that node. At this point, rightSide will have the last nodee that was in our current level of the q
                    q.append(node.left)  # since the node is not null, we will append its children to our queue!
                    q.append(node.right)  # if these children are null? well the above if node: takes care of that!
                # At the end of the for loop, rightSide will hold the rightmost node at the current level because the loop processes nodes from left to right.


            if rightSide:  # if right side is not empty, append it to our result!
                res.append(rightSide.val)
        
        return res

                
            
            
