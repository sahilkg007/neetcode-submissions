class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charset = set()
        # res = 0

        # for i in range(len(s)):
        #     if s[i] in charset:
        #         charset.remove(s[i])
        #     else:
        #         res+=1
        # return res


        res = 0 
        for i in range(len(s)):
            charset = set()
            for j in range(i,len(s)):
                if s[j] in charset:
                    break
                charset.add(s[j])
            res = max(res,len(charset))
        return res
            