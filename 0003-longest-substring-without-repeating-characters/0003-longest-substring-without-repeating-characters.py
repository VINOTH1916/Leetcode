class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        ans = i = 0
        myset = set()

        for j in range(len(str)):
            while str[j] in myset:
                myset.remove(str[i])
                i += 1

            ans = max(ans, j-i+1)
            myset.add(str[j])

        return ans

