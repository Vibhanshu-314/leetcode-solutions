class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        can_eat=len(candyType)//2
        candyType=set(candyType)
        return min(len(candyType),can_eat)
        
