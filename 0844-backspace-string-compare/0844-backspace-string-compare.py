class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def fun(string):
            stack=[]
            for ch in string:
                if ch!="#":
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack   
        return fun(s)==fun(t)

        def fun(string):
            stack=[]
            for ch in string:
                if ch=="#":
                    stack.pop()
                else :
                    stack.append(ch)
            return stack   
        return fun(s)==fun(t)        