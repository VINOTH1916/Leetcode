class Solution:
    def isPalindrome(self, strs: str) -> bool:
        left = 0
        right = len(strs)-1
        
        while left < right:
            while left < right and not strs[left].isalnum():
                left += 1
            
            while left < right and not strs[right].isalnum():
                right -= 1
                
            if strs[left].lower() != strs[right].lower():
                return False
            
            left += 1
            right -= 1
                
        return True
            
                
        
        