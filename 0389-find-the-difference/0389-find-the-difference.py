class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq={}
        for ch in t:
            freq[ch]=freq.get(ch,0)+1
        
        for ch in s:
            freq[ch]=freq.get(ch,0)-1
        for ch,value in freq.items():
            if value==1:
                return ch  
