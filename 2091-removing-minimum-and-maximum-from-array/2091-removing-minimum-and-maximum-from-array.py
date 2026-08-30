class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target=0

        min_nums=float('inf')
        curr_min=nums[0]
        curr_max=nums[0]
        max_nums=float('-inf')
        min_index=0
        max_index=0
        for i in range(len(nums)):
            if nums[i]<curr_min:
                curr_min=nums[i]
                min_nums=min(min_nums,curr_min)
                min_index=i
                
                
            if  nums[i]>curr_max:
                curr_max=nums[i]
                max_nums=max(curr_max,max_nums) 
                max_index=i
        left=min(min_index,max_index)
        right=max(min_index,max_index)
        target=min(len(nums)-left,right+1,left+1+(len(nums)-right))

        return target