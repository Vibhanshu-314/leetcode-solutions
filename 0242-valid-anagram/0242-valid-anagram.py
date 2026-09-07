#from collections import Counter # method 1

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       ## return Counter(s.lower())==Counter(t.lower()) # method 1\
       # # method 2 using the dict
     #   if len(s)!=len(t):
     #     return False

     #   count={}
     #   for ch in s:
     #       count[ch]=count.get(ch,0)+1
     #   for ch in t:
     #       count[ch]=count.get(ch,0)-1 
     #   for value in count.values():
     #       if value!=0:
     #           return False
    #           break
     #   return True               

        if len(s)!=len(t):
          return False
        freq1={}
        freq2={}
        for ch in s:
            freq1[ch]=freq1.get(ch,0)+1

        for ch in t:
            freq2[ch]=freq2.get(ch,0)+1

        return freq1==freq2        
