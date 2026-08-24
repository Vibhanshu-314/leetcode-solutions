class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        max_candie=max(candies)
        for i in range(len(candies)):
            new_candies=candies[i]+extraCandies
            if new_candies>=max_candie:
                result.append(True)
            else:
                result.append(False)    
        return result        
            