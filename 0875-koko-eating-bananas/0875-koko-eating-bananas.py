class Solution: 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def helper(sp,piles):
            rq = 0
            for i in range(len(piles)):
                rq += math.ceil(piles[i]/sp)
            return rq

        left, right = 1, max(piles)
        ans = -1
        while left <= right:
            mid = (left + right)//2
            k = helper(mid,piles)

            if k <= h:
                ans = mid
                right = mid -1
            else:
                left = mid + 1


        return ans

