class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(len(nums)):
            j = i
            while j >= 0:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
                j-=1
        return max(dp)
