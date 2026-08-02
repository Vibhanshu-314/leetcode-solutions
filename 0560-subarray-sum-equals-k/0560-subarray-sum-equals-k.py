class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # brute force approach
      #total=0
      #count=0
      #for i in range(len(nums)):
      #    total=0
      #    for j in range(i,len(nums)):
      #        total+=nums[j]

      #        if total==k:
      #            count+=1
      #return count            






        freq={0:1}
        curr_sum=0
        count=0
        for num in nums:
            curr_sum+=num
            
            if curr_sum-k in freq:
                count+=freq[curr_sum-k]
                
        
            freq[curr_sum]=freq.get(curr_sum,0)+1
        return count