class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n==0:
            return False
        index=n//2
        mid=nums[index]
        
        count=0
        for num in nums:
            if num==mid:
                count+=1
        return count==1        