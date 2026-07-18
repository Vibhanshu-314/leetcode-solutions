class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        water=0
        while left<right:
            if leftmax<rightmax:
                left+=1

                leftmax=max(leftmax,height[left])

                water+=leftmax-height[left]
            else:
                right-=1

                rightmax=max(rightmax,height[right])

                water+=rightmax-height[right]
        return water    
      






    #    if not height:
    #       return 0
#
    #    left = 0
    #    right = len(height) - 1
#
    #    leftMax = 0
    #    rightMax = 0
#
    #    water = 0
#
    #    while left < right:
#
    #        if height[left] < height[right]:
#
    #            if height[left] >= leftMax:
    #                leftMax = height[left]
    #            else:
    #                water += leftMax - height[left]
#
    #            left += 1
#
    #        else:
#
    #            if height[right] >= rightMax:
    #                rightMax = height[right]
    #            else:
    #                water += rightMax - height[right]
#
    #            right -= 1
#
    #    return water