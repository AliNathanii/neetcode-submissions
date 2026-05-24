# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# In-order: Left Sbtree -> Root -> Right Subtree
# Pre-order: Root -> Left Subtree -> Right Subtree
# Post-order: Left Subtree -> Right Subtree -> Root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Recursive thats why we will have a base case at the top:
        if not preorder or not inorder:  # if either one of them is empty
            return None

        # Otherwise we will have to create a tree:
        root = TreeNode(preorder[0])  # the node of this tree will have the first value in our preorder list.
        mid = inorder.index(preorder[0]) # finding above value's (preorder[0]) location in the in-order link
        # creating the subtree now - will pass on the new inorder and preorder lists ie original one's subarrays
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])  # preorder will now be from index to index mid. For preorder we will pass it from the beginning to the mid but not inlcding mid.
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])  # for preorder now we wanna add every value after the above preorder subarray ie starting from mid + 1 to end! For inorder we now need start from mid + 1 (remember mid was included in the previous subarray) to the end.
        return root  # root is our tree (with left and right children that we are now returning)


"""
Base case if either one of the arrays are empty return None, 
otherwise make a new tree where root is a new TreeNode that contains first item of preorder array ie preorder[0],
and the mid point will be the index number of that value's position in inorder array! 
Next we create root.left and root.right. 
They both will be created by recursively calling this function.  
For root.left  it uses preorder[1:mid + 1] (excluding the root) and inorder[:mid] (up to but not including the root). 
For root.right , it uses preorder[mid + 1:] (starting after the left subtree) and inorder[mid + 1:] (starting after the root).
"""