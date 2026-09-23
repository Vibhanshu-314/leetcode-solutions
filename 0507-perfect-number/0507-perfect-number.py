class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        div_sum=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
            
               div_sum+=i
               if i!=num//i:
                div_sum+=num//i
        return num==div_sum        