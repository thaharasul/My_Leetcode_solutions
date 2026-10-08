class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        leftmax,rytmax=0,0
        water=0
        while left<right:
            if height[left]<height[right]:
                leftmax=max(height[left],leftmax)
                water+=leftmax-height[left]
                left+=1
            else:
                rytmax=max(height[right],rytmax)
                water+=rytmax-height[right]
                right-=1
        return water
