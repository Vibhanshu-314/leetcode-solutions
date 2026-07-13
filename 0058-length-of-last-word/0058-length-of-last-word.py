class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this will consume extra spaces

      #  words=s.strip().split()
      #  return len(words[-1])

        s=s.strip()
        count=0
        i=len(s)-1
        while i>=0 and s[i]!=" ":
                count+=1
                i-=1
        return count   

