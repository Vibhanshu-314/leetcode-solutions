class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        result=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1

        for i in range(1,len(nums)+1):
            if freq.get(i,0)==0:
                result.append(i)
        return result        
                    