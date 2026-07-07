class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s="".join(ch for ch in str(n) if ch!="0")
        if s=="":
            return 0
        x=int(s)    

        digit_sum=sum(int(ch) for ch in s)
        return x*digit_sum
