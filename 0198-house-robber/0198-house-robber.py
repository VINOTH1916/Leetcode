class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])


        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i] )

        return max(dp[-1], dp[-2])
        