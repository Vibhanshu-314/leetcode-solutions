class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        freq={}
        result=0  
        for ch in stones:
            freq[ch]=freq.get(ch,0)+1
          
        for ch in jewels:
            result+=freq.get(ch,0)
        return result    