class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        length=0
        odd=False
        for value in freq.values():
            if value%2==0:
                length+=value
            else:
                length+=value-1
                odd=True
        if odd:
            length+=1
        return length    



