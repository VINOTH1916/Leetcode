class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
       left = 0
       res = 0
       myset = set()
       
       for right in range(len(str)):
            while str[right] in myset:
                myset.remove(str[left])
                left += 1
            myset.add(str[right])
            res = max(res, right - left + 1)
       return res
