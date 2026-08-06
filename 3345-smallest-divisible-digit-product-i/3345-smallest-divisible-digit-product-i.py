class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """

        def product(num):

            product=1
            while num>0:
                
               digit=num%10
               product=product*digit
               num=num//10
            return product 
        num=n
        while True:
            if product(num)%t==0:
                return num
            num+=1          
