class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # index=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[index],nums[i]=nums[i],nums[index]
        #         index+=1
        # print(nums)        
        i=0
        for j in range(len(arr)):
           if arr[j]!=0:
             arr[i]=arr[j]
             i+=1
        for k in range(i,len(arr)):
          arr[k]=0
        return arr            