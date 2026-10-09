class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        left = 0
        myset = set()
        ans = 0
        
        for right in range(len(str)):
            while str[right] in myset:
                myset.remove(str[left])
                left += 1
            myset.add(str[right])
            ans = max(ans, right-left+1)
        return ans
            
        
 
        
    