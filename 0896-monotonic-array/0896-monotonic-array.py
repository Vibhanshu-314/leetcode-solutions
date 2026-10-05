class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def inc(nums):
            isvalid=True
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    isvalid=False
            return isvalid        
        def dec(nums):
            isvalid=True
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    isvalid=False
            return isvalid        
        return inc(nums) or dec(nums)                   
       