class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        res = 0
        
        for num in mySet:
            if num - 1 in mySet:
                continue
            else:
                count = 1
                while num + 1 in mySet:
                    count += 1
                    num += 1
                res = max(count,res)
                
        return res
            
                
