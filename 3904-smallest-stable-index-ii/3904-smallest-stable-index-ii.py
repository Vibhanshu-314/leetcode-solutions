class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        suffixMin=[0]*len(nums)
        suffixMin[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suffixMin[i]=min(suffixMin[i+1],nums[i])
        prefixMax=nums[0] 
        for i in range(len(nums)):
            prefixMax=max(prefixMax,nums[i])
            if (prefixMax-suffixMin[i])<=k:
                return i
        return -1        
