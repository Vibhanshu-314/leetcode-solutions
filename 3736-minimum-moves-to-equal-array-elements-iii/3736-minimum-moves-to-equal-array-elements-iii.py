class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num=max(nums)

        moves=0
        for num in nums:
            move=max_num-num
            moves+=move
        return moves    