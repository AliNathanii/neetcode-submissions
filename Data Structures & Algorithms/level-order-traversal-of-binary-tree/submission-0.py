# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """We need to implement BFS Algorithm"""

        res = []  # initialize the result list that will eventually be returned

        q = collections.deque()  # this is how you build a queue in python
        q.append(root)  # adding our given root in the queue.

        while q:  # run the while loop as long as our queue is not empty
            qlen = len(q)  # get the length of the queue
            level = []  # this is where value of each node at each level will be appended
            for i in range(qlen):
                node = q.popleft()  # get the value that was added the first in our queue hence popleft (FIFO)
                if node:  # if that node popped is not empty
                    level.append(node.val)  # append that node's value to level list
                    q.append(node.left)  # appending the left child node of root to our queue
                    q.append(node.right) # appending the right child node of root to our queue
            
            if level:  # again just checking if level is not empty. How/Why level might be empty? Because of None node!
                res.append(level)  # append the level list (of that iteration) to our result list
        
        # Finally we can just return res now
        return res

