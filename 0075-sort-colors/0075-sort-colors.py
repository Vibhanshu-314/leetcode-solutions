class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        index=0 
        for value in [0,1,2]:
            count=freq.get(value,0)
            while count>0:
                nums[index]=value
                index+=1
                count-=1   