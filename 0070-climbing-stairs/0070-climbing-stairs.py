class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
     #  if n==1:
     #      return 1
     #  if n==2:
     #      return 2    
     #  return self.climbStairs(n-1)+self.climbStairs(n-2)   


     # using memo

      # memo={}
      # def dfs(n):
      #     if n==1:return 1
      #     if n==2: return 2
      #     if n in memo: return memo[n]
      #     memo[n]=dfs(n-1)+dfs(n-2)
      #     return memo[n]
      # return dfs(n)    
      #


      # using tabo
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,len(dp)):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]  