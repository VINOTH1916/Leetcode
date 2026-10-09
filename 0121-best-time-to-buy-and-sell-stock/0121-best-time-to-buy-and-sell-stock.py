class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        buy = prices[0]
        
        for p in prices:
            buy = min(buy,p)
            ans = max(ans,p - buy)
            
        return ans
            


















