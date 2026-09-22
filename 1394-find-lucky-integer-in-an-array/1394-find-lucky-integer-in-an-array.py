class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq={}
        max_key=-1
        for num in arr:
            freq[num]=freq.get(num,0)+1
        for key,value in freq.items():
            if key==value:
                max_key=max(max_key,key)
        return max_key    
