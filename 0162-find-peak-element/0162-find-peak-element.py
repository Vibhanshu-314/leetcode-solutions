class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=0
        right=n-1

        while left<right:
            mid=(left+right)//2

            if nums[mid]<nums[mid+1]:
                left=mid+1

            else:
                right=mid
        return left            
            