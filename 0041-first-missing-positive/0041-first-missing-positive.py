class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        while i<n:
            correct_idx=nums[i]-1
            if 1<=nums[i]<=n and nums[correct_idx]!=nums[i]:
                nums[i],nums[correct_idx]=nums[correct_idx],nums[i]

            else:
                i+=1


        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1                    