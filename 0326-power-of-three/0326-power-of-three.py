class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
       # for x in range(1,n):
       #     if n==pow(3,x):
       #         return True
       # return False      
        if  n==1:
            return True
        if n<=0 or n%3!=0:
            return False

        return self.isPowerOfThree(n//3)    
         