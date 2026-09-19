class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result=[]
        for word in words:
          h1={}
          h2={}
          valid=True
          for i in range(len(word)):
            if word[i] not in h2:
              h2[word[i]]=pattern[i]
            if pattern[i] not in h1:
              h1[pattern[i]]=word[i]
            if h1[pattern[i]]!=word[i] or h2[word[i]]!=pattern[i]:
              valid=False
              break
          if valid:

            result.append(word)
        return result        