class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original=n
        digit_sum=0
        product=1
        while n>0:
           last=n%10
           digit_sum+=last
           product=product*last
           n=n//10
        return original %(digit_sum+product)==0