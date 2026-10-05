class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        mf = 0
        j = 0
        freq = defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1
            mf = max(mf,freq[s[i]])
            while (i - j + 1 - mf) > k:
                freq[s[j]] -= 1
                j += 1
                mf = max(freq.values())
           
            ans = max(ans,i-j + 1)
                

        return ans 

