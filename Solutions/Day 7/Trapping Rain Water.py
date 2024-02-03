class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]
        total=0
        l,r=0,len(height)-1
        while l<r:
            if maxL<maxR:
                total += max(maxL-height[l],0)
                l+=1
                maxL = max(maxL,height[l])
            else:
                total += max(maxR-height[r],0)
                r-=1
                maxR = max(maxR,height[r])
        return total    