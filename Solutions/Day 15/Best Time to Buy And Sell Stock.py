class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float("inf")
        profit=0
        for p in prices:
            profit = max(profit, p-cur_min)
            cur_min = min(p,cur_min)
        return profit    
