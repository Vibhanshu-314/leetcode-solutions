class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=999:
            return 0
        else:    
            return n-999
    
