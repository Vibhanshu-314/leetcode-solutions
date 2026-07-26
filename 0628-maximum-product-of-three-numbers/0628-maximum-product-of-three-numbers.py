class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=float('-inf')
        max2=float('-inf')
        max3=float('-inf')
        min1=float('inf')
        min2=float('inf')
        
        
        for i in range(len(nums)):
            if nums[i]>max1:
                max3=max2
                max2=max1
                max1=nums[i]
            elif nums[i]>max2:
                max3=max2
                max2=nums[i]
            elif nums[i]>max3:
                max3=nums[i]
             
                
            # max1=5, max2=2
            if nums[i]<min1:
                min2=min1
                min1=nums[i]
                
            elif nums[i]<min2:
                min2=nums[i]
        return max(max1*max2*max3,max1*min1*min2)  
                
                
                
                