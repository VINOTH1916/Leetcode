class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [-1] * len(nums)
        def helper(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0],nums[1])

            if dp[n] != -1:
                return dp[n]

            best = max(helper(n-1), helper(n-2) + nums[n])
            dp[n] = best
            return best

        return helper(len(nums)-1)
        