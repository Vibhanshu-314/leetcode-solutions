class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        s=s.split()
        if len(s)!=len(pattern):
            return False
        h1={}
        h2={}
        for i in range(len(pattern)):
            if pattern[i] not in h1:
                h1[pattern[i]]=s[i]
            if s[i] not in h2:
                h2[s[i]]=pattern[i]
            if h1[pattern[i]]!=s[i] or h2[s[i]]!=pattern[i]:
                return False
        return True                
