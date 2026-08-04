class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max=nums[0]
        min=nums[0]
        
        for i in range(1,len(nums)):
            if nums[i]>max:
                max=nums[i]
            elif nums[i]<min:
                min=nums[i]
        result=[]
        for num in range(min,max+1):
            if num not in nums:
                result.append(num)
        return result       
