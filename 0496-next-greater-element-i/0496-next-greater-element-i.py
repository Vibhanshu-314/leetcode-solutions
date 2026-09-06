class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #nge={} # isse storage problem ni hoga    ek nums 1 main last main  changes kr denge
        #stack=[]
        #for num in nums2:
        #    while stack and stack[-1]<num: # check empty toh nhi hai na and pichla element #chota ho  agle se toh map krdo  wrna loop se bhr  rho  or bss num ko append krdo #stack main
        #       nge[stack.pop()]=num
        #    stack.append(num)     # kuch element reh jayenge jinke right side kuch nhai hoga #toh woh stack m hi reh jayenge 
        #while stack:#  toh unko ab hum last main khud map kr denge -1   
        #    nge[stack.pop()]=-1
        #res=[]
        #
        #for num in nums1:
        #    res.append(nge[num]) # bs res main append krdo unki value ko bss  
#
        #return res   




        i=0
        arr=[]
        while i<len(nums1):
           j=nums2.index(nums1[i])
           j+=1
           while j<len(nums2):
             if nums2[j]>nums1[i]:
               arr.append(nums2[j])
               break
             j+=1 
           else:
             arr.append(-1)
           i+=1    

        return arr         