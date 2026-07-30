class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        s_row=0
        e_row=len(matrix)-1
        
        s_col=0
        e_col=len(matrix[0])-1
        
        ans=[]
        
        
        while s_row<=e_row and s_col<=e_col:
            
            # for top part
            for j in range(s_col,e_col+1):
                ans.append(matrix[s_row][j])
                
            s_row+=1
            
            for i in range(s_row,e_row+1):
                ans.append(matrix[i][e_col])
                
            e_col-=1
            if s_row<=e_row:
            
               for j in range(e_col,s_col-1,-1):
                   ans.append(matrix[e_row][j])
               e_row-=1
            if s_col<=e_col:

               for i in range(e_row,s_row-1,-1):
                   ans.append(matrix[i][s_col])
               s_col+=1

        return ans