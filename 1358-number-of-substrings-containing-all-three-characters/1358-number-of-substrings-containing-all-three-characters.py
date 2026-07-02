class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        count=0
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while len(freq)==3:
                count+=len(s)-right
                freq[s[left]]-=1

                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
        return count             