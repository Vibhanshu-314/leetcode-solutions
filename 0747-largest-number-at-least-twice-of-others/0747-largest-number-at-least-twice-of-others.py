class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=float('-inf')
        sec=float('-inf')
        index=-1
        for i  in range(len(nums)):
            if nums[i]>first:
                sec=first
                first=nums[i]
                index=i

            elif nums[i]>sec:
                sec=nums[i]
        if first>=(2*sec):
            return index
        else:
            return -1             