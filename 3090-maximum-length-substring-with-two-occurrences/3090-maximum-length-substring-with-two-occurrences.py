class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        freq={}
        max_len=0
        for right in range(len(s)):
            ch=s[right]
            freq[ch]=freq.get(ch,0)+1
            
            while freq[ch]>2:
                freq[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len    