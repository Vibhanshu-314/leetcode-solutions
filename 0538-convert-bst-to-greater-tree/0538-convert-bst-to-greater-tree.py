# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.total=0
        def revOrder(node):
            if node is None:
                return 
            revOrder(node.right)

            self.total+=node.val
            node.val=self.total

            revOrder(node.left)
        revOrder(root)
        return root        