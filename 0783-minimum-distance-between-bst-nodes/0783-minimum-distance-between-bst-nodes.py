# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev=None
        self.minimum=float('inf')

        def inorder(node):
            if node is None:
                return
            inorder(node.left)

            if self.prev is not None:
                self.minimum=min(self.minimum,node.val-self.prev)

            self.prev=node.val    

            inorder(node.right)

        inorder(root)
        return self.minimum            