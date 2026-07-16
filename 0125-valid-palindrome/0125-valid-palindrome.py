class Solution:
    def isPalindrome(self, strs: str) -> bool:
        res = ""
        for s in strs:
            if s.isalnum():
                res += s
        return res.lower() == res[::-1].lower()
            
                
        
        