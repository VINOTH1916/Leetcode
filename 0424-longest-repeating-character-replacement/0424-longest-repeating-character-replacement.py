class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        r = 0
        maxfreq = 0
        hmap = defaultdict(int)

        for l in range(len(s)):
            hmap[s[l]] += 1
            maxfreq = max(maxfreq,hmap[s[l]])
            while (l-r + 1 - maxfreq) > k:
                hmap[s[r]] -= 1
                maxfreq = max(hmap.values())
                r += 1


            res = max(res, l-r+1)


        return res
                
