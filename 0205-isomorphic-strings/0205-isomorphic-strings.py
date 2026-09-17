class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False 
        hash1={}
        hash2={}


        for i in range(len(s)):
            if s[i] not in hash1:

                hash1[s[i]]=t[i] 

            if t[i] not in hash2:
                hash2[t[i]]=s[i]    
            if hash1[s[i]]!=t[i] or hash2[t[i]]!=s[i]:
                return False
        return True        
