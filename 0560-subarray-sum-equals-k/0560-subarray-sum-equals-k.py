class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        mp = {0: 1}
        ans = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in mp:
                ans += mp[curr_sum - k]

            mp[curr_sum] = mp.get(curr_sum, 0) + 1

        return ans