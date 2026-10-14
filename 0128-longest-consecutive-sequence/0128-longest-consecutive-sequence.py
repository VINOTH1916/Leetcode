class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        count = 1
      
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                count = 1
            
            res = max(count,res)
            
        return res
        
                
                
                
        
        
            
                
