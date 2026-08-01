class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False

        i=0    
        while pow(4,i)<=n:
            if pow(4,i)==n:
                return True
            i+=1
        return False        