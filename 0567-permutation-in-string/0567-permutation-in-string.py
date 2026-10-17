class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def hashmap(s):
            mp = defaultdict(int)
            for a in s:
                mp[a]+=1
            return mp

        ls = hashmap(s1)
        for i in range(len(s1),len(s2)+1):
            if ls == hashmap(s2[i-len(s1):i]):
                return True
        return False

        