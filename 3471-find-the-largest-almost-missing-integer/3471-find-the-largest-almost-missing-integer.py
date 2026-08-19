class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={}
        
        for i in range(len(nums)-k+1):
            seen=set(nums[i:i+k])

            for num in seen:
                count[num]=count.get(num,0)+1



        ans=-1
        for num,freq in count.items():
            if freq==1:
                ans=max(ans,num)
        return ans                


