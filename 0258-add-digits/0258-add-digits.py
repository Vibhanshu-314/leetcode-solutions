class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            ans=0
            while num>0:
                last=num%10
                ans+=last
                num=num//10
            num=ans
        return num        

       
         