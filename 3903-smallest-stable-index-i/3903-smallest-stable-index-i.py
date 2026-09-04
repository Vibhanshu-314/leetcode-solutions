class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        for i in range(len(nums)):
          max_val=max(nums[:i+1])
          min_val=min(nums[i:])
          score=max_val-min_val
          if score<=k:
            return i
        return -1    
               
             
          
  