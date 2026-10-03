class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def word_freq(word):
        
          freq={}
          for ch in word:
            
             freq[ch]=freq.get(ch,0)+1
          return freq
          
          
        current=word_freq(words[0])  
          
          
        for word in words[1:]:
          freq=word_freq(word)
        
        
          for ch in current:
            if ch in freq:
              current[ch]=min(current[ch],freq[ch])
            else:
              current[ch]=0
        res=[]
        
        for ch in current:
          for _ in range(current[ch]):
            res.append(ch)        
        return res    