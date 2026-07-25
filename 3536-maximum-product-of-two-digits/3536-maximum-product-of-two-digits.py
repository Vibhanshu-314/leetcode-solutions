class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # phle hum bhtyi hum ek kaam krte hai ki first and second greater element nikal lete hai

        first=0
        second=0
        
        while n:
            digit=n%10
            if digit>first:
                # yeh isliye kiya jissse  purana first kho na jye 
                second=first
        
                first=digit

            elif digit>second:
                second =digit

            n=n//10

        return first*second            

