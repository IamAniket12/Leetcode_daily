import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right = max(piles)
        ans = float("inf")
        while left<=right:
            mid = (left+right)//2
            temp = 0
            for p in piles:
                temp+=math.ceil(p/mid)
            if temp<=h:
                ans = min(ans,mid)
                right=mid-1
            else:
                left=mid+1
        return ans                 

        