class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def divide(num):

            n=num
            while num>0:
                last=num%10
                if last==0:
                    return  False
                if n%last!=0:
                    return False
                num//=10
            return True

        def check(left,right):
            ans=[]
            for num in range(left,right+1):
                if divide(num):
                    ans.append(num) 
            return ans
        return check(left,right)            

