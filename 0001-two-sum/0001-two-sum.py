class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap={}
        # for i,num in enumerate(nums):
        #  complement=target-num
        #  if  complement in hashmap:
        #     return [hashmap[complement],i]
        #  hashmap[num]=i    

        seen={}
        for i in range(len(nums)):
          comp=target-nums[i]
          if comp in seen:
            return [seen[comp],i]
          else:
            seen[nums[i]]=i  