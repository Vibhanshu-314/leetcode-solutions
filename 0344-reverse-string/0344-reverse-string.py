class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
      #stack=[]
      #for ch in s:
      #    stack.append(ch)
      #for i in range(len(stack)):
      #    s[i]=stack.pop()   

        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s    