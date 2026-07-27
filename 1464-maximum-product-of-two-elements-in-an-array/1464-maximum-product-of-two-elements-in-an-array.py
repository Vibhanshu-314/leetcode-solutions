class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max1=nums[0]
        max2=0



        for i in range(1,len(nums)):
            if nums[i]>max1:
                max2=max1
                max1=nums[i]

            elif nums[i]>max2:
                max2=nums[i]    
        return (max1-1)*(max2-1)        



                