class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # n=len(nums)
        # nums.sort()
        # res=[]
        # for i in range(n-2):
        #     if (i>0 and nums[i]==nums[i-1]):
        #         continue

        #     j=i+1
        #     k=n-1

        #     while(j<k):
        #         total=nums[i]+nums[j]+nums[k]

        #         if total>0:
        #             k-=1
        #         elif total<0:
        #             j+=1

        #         else:
        #             res.append([nums[i],nums[j],nums[k]])

        #             j+=1
        #             k-=1
        #             while (j<k and nums[j]==nums[j-1]):
        #                 j+=1
        # return res
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            # for resolving thr prblm of the duplicate
          if i>0 and nums[i]==nums[i-1]:
            continue

          left=i+1
          right=len(nums)-1
          while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if sum==0:
              result.append([nums[i],nums[left],nums[right]])
              left+=1
              right-=1
              while left<right and nums[left]==nums[left-1]:
                left+=1
              while left<right and nums[right]==nums[right+1]:
                right-=1  

            elif sum<0:
              left+=1
            else:
              right-=1
        return result    
              