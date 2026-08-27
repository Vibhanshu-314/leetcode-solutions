class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       # freq={}
       # for i in nums:
       #     freq[i]=freq.get(i,0)+1

       # for key,value in freq.items():
       #     if value>len(nums)//2:
       #         return key   


        number=None
        count=0
        for num in nums:
            if count==0:
                number=num
            if num==number:
                count+=1
            else:
                count-=1
        return number                