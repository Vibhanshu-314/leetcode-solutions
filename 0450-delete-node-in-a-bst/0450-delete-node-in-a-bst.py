# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # basically this question is tough beacuse  we have to delete the node and then connect the others  too 
       # and we also have 3 conditons like after deletion   we will face three condition for children
       
        # lets start 
        if root is None:
            return None
     
        # checking where does key lies
        if root.val>key:
            #if the value of the key is smallerr  maens it wil liew inthe left side of the root  sccording to bst 
            root.left=self.deleteNode(root.left,key)  
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)

        else:
            # key==root.val
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            curr=root.right
            while curr.left:
                curr=curr.left
            root.val=curr.val

            root.right=self.deleteNode(root.right,curr.val)
        return root                   