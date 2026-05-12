class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        # res = 0

        for i in range(len(s)):
            if s[i] in charset:
                charset.remove(s[i])
            else:
                charset.add(s[i])
                
        return len(charset)


            