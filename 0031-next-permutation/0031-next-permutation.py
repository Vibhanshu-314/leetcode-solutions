class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # phle toh pvt point dhkena hai 

        # last se check krte hia
        n=len(nums)
        pvt=-1
        for i in range(n-2,-1,-1):
            # n-2 isliye   kyuki hum check kr rhe hai next elemnet ke liey last ka next ha hi ni toh s-2 ke liye kr rhe hai
            if nums[i]<nums[i+1]:
                pvt=i

                break
        # bhyi agr nums ke main values sare decresing m ho toh next permutation original wala hi hog a

        if pvt==-1:
            nums.reverse()  # direct return nums isliye ni kiya kyuki hum in place change kr rhe ahi 

            return        


        # abb pvtt pe jo value hai uska next  greater value chaiye
        for i in range(n-1,pvt,-1):
            if nums[i]>nums[pvt]:
              nums[i],nums[pvt]=nums[pvt],nums[i]
              break
        # ab kam reh gya ki baki value ko increasing order ya keh skte hai ek smallest number main bnanan hai

        left=pvt+1
        right=n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left] 
            left+=1
            right-=1

