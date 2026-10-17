class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def hashmap(stri):
            fm = defaultdict(int)
            for ch in stri:
                fm[ch] += 1
            return fm
            
        s1_fm = hashmap(s1)
        
        j = len(s1)
        
        for i in range(len(s2)-len(s1)+1):
            if s1_fm == hashmap(s2[i:j]):
                return True
            j+=1
        return False