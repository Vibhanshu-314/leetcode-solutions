# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        ans=[]
        queue=deque([root])
        level_number=0

        while queue:
            
            level=[]
            level_size=len(queue)
            
            for _ in range(level_size):
                
                node=queue.popleft()
                level.append(node.val)
                
               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_number+=1
            if level_number%2==0:
              level.reverse()        
                
            ans.append(level)

        return ans                
        