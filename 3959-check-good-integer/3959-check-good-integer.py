class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit_sum=0
        square_sum=0
        while n>0:
            last_digit=n%10
            digit_sum+=last_digit
            square_sum+=(last_digit)**2
            n=n//10
        if (square_sum-digit_sum)>=50:  
            return True
        return False      