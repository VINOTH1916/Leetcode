class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        left = count = right = 0
        hmap = defaultdict(int)

        for ch in t:
            hmap[ch] += 1
    
        minlen = float('inf')
        sidx = -1

        while right < len(s):
            if hmap[s[right]] > 0:
                count += 1
            hmap[s[right]] -= 1
            while count == len(t):
                if (right - left + 1) < minlen:
                    minlen = right - left + 1
                    sidx = left
                hmap[s[left]] += 1
                if hmap[s[left]] > 0:
                    count -= 1
                left += 1

            right += 1
        

        return "" if sidx == -1 else s[sidx:sidx + minlen]
            


        