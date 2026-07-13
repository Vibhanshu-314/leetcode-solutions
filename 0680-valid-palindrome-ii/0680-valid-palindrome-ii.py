class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True        
        left,right=0,len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
               return  check(left + 1, right) or check(left, right - 1)
        return True       