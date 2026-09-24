class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int

        """
        freq={}
        for i in range(1,n+1):
            digit_sum=0
            while i>0:
                digit_sum+=i%10
                i=i//10
            freq[digit_sum]=freq.get(digit_sum,0)+1
        max_freq=0
        ans=0
        for key,value in freq.items():
            if value>max_freq:
                max_freq=value
                ans=1
            elif value==max_freq:
                ans+=1
        return ans                    