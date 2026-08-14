class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        # recursion

       #if n<=1:
       #    return n
       #return self.fib(n-1) + self.fib(n-2)       

        # memoziation 
        memo={}
        def dfs(n):
            if n<=1:
                return n
            if n in memo:
                return memo[n] 
            memo[n]=dfs(n-1)+dfs(n-2)
            return memo[n]
        return dfs(n)       