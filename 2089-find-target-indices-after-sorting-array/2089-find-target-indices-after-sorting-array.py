class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        while nums:
          min_num=nums[0]
          for num in nums:
            if num<=min_num:
              min_num=num
              
          result.append(min_num)
          nums.remove(min_num)
        ans=[]  
        for i,num in enumerate(result):
          if target==num:
            ans.append(i)
        return ans    
            
            