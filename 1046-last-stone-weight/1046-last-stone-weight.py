class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
           stone1=0
           stone2=0
           for stone in stones:
               if stone>=stone1:
                   stone2=stone1
                   stone1=stone
               elif stone>stone2:
                   stone2=stone
           stones.remove(stone1)
           stones.remove(stone2)
   
           if stone1!=stone2:
               stones.append(stone1-stone2)
        return stones[0] if stones else 0