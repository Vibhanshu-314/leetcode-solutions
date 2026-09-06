class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                sum+=nums[i]
            else:
                break


        while sum in nums:
            sum+=1
        return sum              