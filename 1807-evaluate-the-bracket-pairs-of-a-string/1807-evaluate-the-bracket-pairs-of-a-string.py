class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d={}
        for i in knowledge:
           d[i[0]]=i[1]
          
        i=0
        ans=""
        while i<len(s):
            if s[i]=="(":
                j=i+1

                while s[j]!=")":
                    j+=1
                key=s[i+1:j]

                if key in d:
                    ans+=d[key]

                else:
                    ans+="?"
                i=j+1
            else:
                ans+=s[i]

                i+=1
        return ans                    


