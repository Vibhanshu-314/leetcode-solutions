class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_total=sum(aliceSizes)
        bob_total=sum(bobSizes)
        difference=(bob_total-alice_total)//2
        bob_set=set(bobSizes)
        for a in aliceSizes:
            b=a+difference
            if b in bob_set:
                return [a,b]   
