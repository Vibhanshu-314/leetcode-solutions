# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result=[]
        def dfs(node,remain,path):
            if node is None:
                return
            path.append(node.val)

            if node.left is None and node.right is None:
                if remain==node.val:
                    result.append(list(path))
            dfs(node.left,remain-node.val,path)
            dfs(node.right,remain-node.val,path) 

            path.pop()

        dfs(root,targetSum,[])
        return result               