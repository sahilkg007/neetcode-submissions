class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charset:
                l+=1
            else:
                charset.add(s[r])
            r+=1
            res = max(res,r-l)
        return res