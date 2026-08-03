class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[1]*n
        prefix=[1]*n
        suffix=[1]*n


        # phle age walw mtlb left main sare multipy krdo

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1] # nums[i-1] isliye kyuki khuda product ni krna toh usse ek phle tk krdo

            # fhir abb usse ageke right wale product krdoo   

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1] # nums[i+1] isliye kyuki khud ka ni krna nnaaa isliye usse right ma jo hai unka   
        for i in range(n):
            ans[i]=suffix[i]*prefix[i]        

        return ans    