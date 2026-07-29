class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # brute for kya hogi
        # phle find krenge index i and j jha 0 aa rha hai 
        # fhir in place change kr denge  jha ya toh i same hoga ya toh j same hoga
        
        row=set()
        column=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    column.add(j)
        # matrix = [[1,1,1],[1,0,1],[1,1,1]]            
        # abb   row=(1), column=(1)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                    matrix[i][j]=0
                                