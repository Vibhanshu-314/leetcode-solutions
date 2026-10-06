class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def getfreq(str):
            freq={}
            for ch in str:
                freq[ch]=freq.get(ch,0)+1
            return tuple(sorted(freq.items()))
        group={}
        for word in strs:
            key=getfreq(word)
            if key not in group:
                group[key]=[]
            group[key].append(word)
        return group.values()              