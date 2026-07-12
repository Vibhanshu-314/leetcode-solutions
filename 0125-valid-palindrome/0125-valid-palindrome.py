class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=''.join(ch.lower() for ch in s  if ch.isalnum())
# this comsumes extra space 
        #return s==s[::-1]
        left,right=0,len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1



        return True        