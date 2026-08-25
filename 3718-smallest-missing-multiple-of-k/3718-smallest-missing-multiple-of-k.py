class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=1
        while True:
            number=k*i
            if number not in nums:
                return number
            i+=1    
