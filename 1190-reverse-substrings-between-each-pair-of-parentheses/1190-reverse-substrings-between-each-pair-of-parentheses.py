class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for ch in s:
            if ch!=")":
                stack.append(ch)
            else:
                temp=[]
                while stack[-1]!="(":
                   temp.append(stack.pop())
                stack.pop()

                for c in temp:
                    stack.append(c)
        return "".join(stack)                    