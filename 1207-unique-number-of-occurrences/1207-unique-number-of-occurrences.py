class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        
        return len(freq)==len(set(freq.values()))
                
